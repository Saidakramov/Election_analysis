# Election_analysis

## Overview of Election Audit 
A Colorado Board of Elections employee provided us with the following tasks to complete election audit of recent local congressional election.
1. How many votes were cast in this congressional election?
2. Provide a breakdown of the number of votes and the percentage of total votes for each county.
3. Which county had the largest number of votes?
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Election-Audit Results
The analysis of the elections shows that:
- That there were 369,711 votes cast in the election.

- The county results were:
  - Jefferson county received 10.5% of the vote and earned 38,855 number of votes.
  - Denver county received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe county received 6.7% of the vote and 24,801 number of votes.
 
- Largest county turnout was Denver county with 306,055 number of votes.
  
- The candidate results were :
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% and 11,606 number of votes.

- The winner of the election was :
  - Diana DeGette received 73.8% of vote and 272,892 number of votes.
 
## Election-Audit Summary
Our script can help the election commission to analyze their future elections by slightly modifying it. For example: 

1)
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

The above code provides a path to load and save files. Users can input a new path inside the parentheses and access new data.

2) If the user wants to access additional data such as ballot IDs, they can access it by setting a ballot_id = [0] and place under the codes below, which will access the first row of columns on the data.
 # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
   
