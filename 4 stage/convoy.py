import pandas as pd
import csv
import sqlite3
import json


def correct_input(file_name, w_file_name, db_file_name):
    if '[CHECKED]' in file_name and '_chk' not in file_name:
        w_file_name = file_name
        db_file_name = file_name.replace("[CHECKED]", "chk").replace(".csv", ".s3db")
    elif '[CHECKED]' in file_name and '_chk' in file_name:
        w_file_name = file_name
        db_file_name = file_name.replace("[CHECKED]", "").replace(".csv", ".s3db")
    return w_file_name, db_file_name


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


def db_create(db_file_name):
    conn = sqlite3.connect(db_file_name)
    c_name = conn.cursor()
    c_name.execute('drop table if exists convoy;')
    return conn, c_name


def db_execution(file_reader, c_name, count):
    for line in file_reader:
        if count == 0:
            headers = tuple(line)
            c_name.execute(f'create table if not exists convoy({headers[0]} int primary key,'
                           f' {headers[1]} int not null, {headers[2]} int not null, {headers[3]} int not null);')
            count = 1
        else:
            values = tuple(line)
            c_name.execute(f'insert into convoy{headers} values{values};')
            count += 1
    return count


def db_close(conn):
    conn.commit()
    conn.close()


def main():
    file_name = input("Input file name\n")
    db_file_name = ''
    if '.s3db' not in file_name:
        w_file_name = ''
        if '[CHECKED]' in file_name:
            w_file_name, db_file_name = correct_input(file_name, w_file_name, db_file_name)
        else:
            if file_name[-4:] == "xlsx":
                my_df = pd.read_excel(str(file_name), sheet_name="Vehicles", dtype=str)
                file_name = file_name[:len(file_name) - 4] + 'csv'
                my_df.to_csv(str(file_name), index=False)
                rows = my_df.shape[0]
                print(f'{rows} line{"s were" if rows != 1 else " was"} added to {file_name}')
            w_file_name = file_name[:len(file_name) - 4] + '[CHECKED].csv'
            correcting(file_name, w_file_name)
            db_file_name = file_name.replace(".csv", ".s3db")
        conn, c_name = db_create(db_file_name)
        with open(w_file_name, 'r') as w_file:
            count = 0
            file_reader = csv.reader(w_file, delimiter=',', lineterminator='\n')
            count = db_execution(file_reader, c_name, count)
        print(f'{count - 1} record{"s were" if count != 2 else " was"} inserted into {db_file_name}')
        db_close(conn)
    else:
        db_file_name = file_name

    conn = sqlite3.connect(db_file_name)
    data_df = pd.read_sql_query("select * from convoy", conn)
    convoy_dict = data_df.to_dict(orient='records')
    js_file_name = db_file_name.replace(".s3db", ".json")
    with open(js_file_name, 'w') as file:
        json.dump({'convoy': convoy_dict}, file)
    length = len(convoy_dict)
    print(f'{length} vehicle{"s were" if length != 1 else " was"} saved into {js_file_name}')
    db_close(conn)


if __name__ == '__main__':
    main()
