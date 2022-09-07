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

<h2>Interface</h2>
The player is able to see the domino snake, the so-called playing field, and their own pieces.
<h4>Examples</h4>

<em>The player makes the first move (status = "player"):</em>
![1](https://user-images.githubusercontent.com/93375843/181848503-f1ed794a-68ba-4d6c-9bf0-3d48f8ff58c0.jpg)

<em>The Computer makes the first move (status = "computer"):</em>

![2](https://user-images.githubusercontent.com/93375843/181848808-e99d1951-984d-4019-be9b-2c7d7338dd45.jpg)
<h2>AI</h2>
The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. To reduce our chances of skipping a turn, we must increase the diversity of our pieces. For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. Using this logic, the AI evaluates each domino in possession, based on the rarity. Dominoes with rare numbers get lower scores, while dominoes with common numbers get higher scores.

The AI uses the following algorithm to calculate the score:

            1. Count the number of 0's, 1's, 2's, etc., in our hand, and in the snake.
            2. Each domino in our hand receives a score equal to the sum of appearances of each of its numbers.
            
The AI now attempts to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI moves down the score list and tries another domino. The AI skips the turn if it runs out of options.
<h4>Example</h4>

![3](https://user-images.githubusercontent.com/93375843/181852470-f74f2c73-7243-450d-b3a2-338239cde22f.jpg)
