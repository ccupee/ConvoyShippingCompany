# ConvoyShippingCompany
# Dominoes
Classic dominoes game against a computer.
In this project artificial intelligence can make use of simple statistics to make educated decisions. 

<h2>Objectives</h2>

<div style=”margin-left:20px;”>1. Prompt the user to give a name for the input file (complete with the .xlsx, .csv, [CHECKED].csv or .s3db extension). For the prompt message, use Input file name followed by a newline.</div>  



<div style=”margin-left:20px;”>2. If your file is .xlsx or .csv, or it ends with %...%[CHECKED].csv, perform:</div>

    a.If your file is .xlsx, convert it to .csv.
    b.If your file is .csv correct the data right in the file.
    c.Every cell of the output file, except headers, should contain only one integer number.
    d.Count the number of the cells corrected by your script.
    e.Write the corrected data to a CSV file, add the [CHECKED] suffix to your file. For example: %file_name%[CHECKED].csv.
    f.Your program should output the following message for the converted CSV file: X cells were corrected or 1 cell was corrected, where X is the number of corrected       cells. Include the output file name.
    For example: 4 cells were corrected in %file_name%[CHECKED].csv.


<div style=”margin-left:20px;”>3. If the file ends with %...%[CHECKED].csv, create an SQLite3 database with the CSV file name, change its extension to .s3db. Remove the [CHECKED] suffix. For example, %file_name%[CHECKED].csv should be changed to %file_name%.s3db.</div>


<div style=”margin-left:20px;”>4. Use "convoy" as the name for your database table and headers from the CSV file as the names of the table columns.</div>

<div style=”margin-left:20px;”>5. The vehicle_id column should have the INTEGER type; make sure it's PRIMARY KEY, other columns should have the INTEGER type with NOT NULL attributes.</div>

<div style=”margin-left:20px;”>6. Insert the entries from your %...%[CHECKED].csv file. Count the number of entries inserted into the database.
    Your program should output the following message: X records were inserted or 1 record was inserted, where X is a number of inserted records and the output file         name. For example: 4 records were inserted into %file_name%.s3db.</div>
    
<div style=”margin-left:20px;”>7. Add the score column to .s3db files. Populate the column with the scoring points, according to the algorithm described above. The score column should be added during the conversion from %...%[CHECKED].csv to .s3db.</div>

<div style=”margin-left:20px;”>8. Generate JSON and XML files according to the scoring points. All entries with a score of greater than 3 should be exported to the JSON file, others to the XML file. The score column should not be exported to JSON and XML files.</div>

<div style=”margin-left:20px;”>9. Count the number of entries imported to JSON and XML files.
    Your program should output the following message: X vehicles were saved or 1 vehicle was saved, where X is the number of inserted entries. The program should           include the output file name.</div> For example: 9 vehicles were saved into %file_name%.json
                                               0 vehicles were saved into %file_name%.xml</div>

<h4>Examples</h4>
![12](https://user-images.githubusercontent.com/93375843/188939540-560ead20-7fcd-4f3e-94b5-6615abf897ca.jpg)

<em>XLSX file data_final_xlsx.xlsx</em>
![13](https://user-images.githubusercontent.com/93375843/188939566-0c00be29-3685-483f-898f-e90dd8767afa.jpg)

<em>CSV file data_final_xlsx[CHECKED].csv</em>
![14](https://user-images.githubusercontent.com/93375843/188939586-421dbaf0-72a7-43c7-9f91-7c612351c021.jpg)

![11](https://user-images.githubusercontent.com/93375843/188939612-86971aa6-65f1-4b61-8554-7dded9613aa3.jpg)





