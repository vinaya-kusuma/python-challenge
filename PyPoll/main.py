#modules
import os
import csv

#initialize the count of total votes 
votes_count = 0
# to store the candidates and the votes won
candidate_list ={}

# Set the File path
csvpath = os.path.join("Resources","election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath,"r",encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    #header
    csvheader = next(csvfile)

     # Read through each row of data after the header
    for row in csvreader:
        #count of votes casted
        votes_count +=1
        candidate_name = row[2]
        
        #if the candidate's name already occurs in the dict,increment the value
        if row[2] in candidate_list:
            candidate_list[candidate_name] +=1
        #if not, then  add the candidate's name to the dict with value 1
        else:
             candidate_list[candidate_name] = 1


#winner of the election based on popular(maximum) vote
winner = max(candidate_list, key=candidate_list.get)

#file content
Line1 = "Election Results"
Line2 ="----------------------------------------"
Line3= f"Total Votes: {votes_count}"
lines = [Line1,Line2,Line3,Line2]


#Print out results to terminal
for line in lines:
     print("\n" + line)

for candidate in candidate_list:
     print(candidate+": " + str(round((candidate_list[candidate]*100)/votes_count,3))+"%" + " ("+str(candidate_list[candidate])+") " +"\n")

print(Line2)
print("\n Winner: " + winner + "\n")
print(Line2)     

#text file that contains the result of the analysis
file_path = "analysis\output.txt"
with open(file_path, "w") as file:
        for line in lines:
             file.write("\n" + line + "\n")

        for key, value in candidate_list.items():
             #calculate percentage of votes won by each candidate
             percentage = round((value*100)/votes_count,3)
             file.write(f"\n {key}: {percentage}% ({value})\n") 

        file.write("\n" + Line2 + "\n")     
        file.write("\n" +"Winner: " + winner + "\n")
        file.write("\n" + Line2)     