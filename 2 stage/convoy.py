import pandas as pd
import csv


def main():
    file_name = input("Input file name\n")
    if file_name[-4:] == "xlsx":
        my_df = pd.read_excel(str(file_name), sheet_name="Vehicles", dtype=str)
        file_name = file_name[:len(file_name) - 4] + 'csv'
        my_df.to_csv(str(file_name), index=False)
        if my_df.shape[0] == 1:
            print(f'{my_df.shape[0]} line was added to {file_name}')
        else:
            print(f'{my_df.shape[0]} lines were added to {file_name}')
    count = 0
    cells = 0
    w_file_name = file_name[:len(file_name) - 4] + '[CHECKED].csv'
    with open(file_name, "r") as r_file,\
        open(w_file_name, "w") as w_file:
        file_reader = csv.reader(r_file, delimiter=",", lineterminator="\n")
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\n")
        for line in file_reader:
            if count == 0:
                file_writer.writerow(line)
                count += 1
            else:
                new_list = []
                for elem in line:
                    if elem.isdigit():
                        new_list.append(elem)
                    else:
                        digits = "".join([i for i in elem if i in '0123456789'])
                        new_list.append(digits)
                        cells += 1
                file_writer.writerow(new_list)
    if cells != 1:
        print(f'{cells} cells were corrected in {w_file_name}')
    else:
        print(f'{cells} cell was corrected in {w_file_name}')


if __name__ == '__main__':
    main()
