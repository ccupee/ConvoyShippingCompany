import pandas as pd


def main():
    file_name = input("Input file name\n")
    my_df = pd.read_excel(str(file_name), sheet_name="Vehicles", dtype=str)
    csv_file = file_name[:len(file_name) - 4] + 'csv'
    my_df.to_csv(str(csv_file), index=None)
    rows = my_df.shape[0]
    if rows == 1:
        print(f'{rows} line was imported to {csv_file}')
    else:
        print(f'{rows} lines were imported to {csv_file}')


if __name__ == '__main__':
    main()
