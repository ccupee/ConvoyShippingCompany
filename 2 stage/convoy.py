import pandas as pd
import csv


def correcting(file_name, w_file_name):
    count = 0
    cells = 0
    with open(file_name, "r") as r_file, open(w_file_name, "w") as w_file:
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
    print(f'{cells} cell{"s were" if cells != 1 else " was"} corrected in {w_file_name}')


def main():
    file_name = input("Input file name\n")
    if file_name[-4:] == "xlsx":
        my_df = pd.read_excel(str(file_name), sheet_name="Vehicles", dtype=str)
        file_name = file_name[:len(file_name) - 4] + 'csv'
        my_df.to_csv(str(file_name), index=False)
        rows = my_df.shape[0]
        print(f'{rows} line{"s were" if rows != 1 else " was"} added to {file_name}')
    w_file_name = file_name[:len(file_name) - 4] + '[CHECKED].csv'
    correcting(file_name, w_file_name)


if __name__ == '__main__':
    main()
