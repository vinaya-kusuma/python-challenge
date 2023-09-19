#modules
import os
import csv

#initializing all the variables
row_count =0
netPLamount =0
previous_pl =0 
greatest_profit_increase = 0
greatest_profit_decrease = 0
pl_change = 0
first_record = True

# Set the File path
csvpath = os.path.join("Resources","budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath,"r",encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    #header
    csvheader = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        #count the rows in the file
        row_count +=1
        #net total amount of "Profit/Losses"
        netPLamount += int(row[1])
        
        #if the row is the first row, no pl difference calculation
        if first_record == True:
            pldiff = 0
            #set the first_record flag to 0 for the next record
            first_record = False

        # pl difference calculation
        else:
            #calculate the PL difference
            pldiff =  int(row[1]) - previous_pl
            #total change in PL 
            pl_change += pldiff

        if  pldiff > greatest_profit_increase:
            greatest_profit_increase = pldiff
            greatest_profit_month = row[0]
        
        if pldiff < greatest_profit_decrease:
            greatest_profit_decrease = pldiff
            greatest_loss_month = row[0]

        #store the pl as previous_pl for the nest record
        previous_pl = int(row[1])
    
    avg_change = round(pl_change/(row_count-1),2)

    #File content
    line1 =  "Financial Analysis \n"
    line2 ="\n---------------------------------------- \n"
    line3= f"\n Total Months: {row_count} \n"
    line4 = f"\n Total: ${netPLamount} \n"
    line5 = f"\n Average Change: ${avg_change} \n"
    line6= f"\n Greatest Increase in Profits: {greatest_profit_month}  (${greatest_profit_increase}) \n"
    line7= f"\n Greatest Decrease in Profits: {greatest_loss_month} (${greatest_profit_decrease}) \n"
    lines = [line1,line2,line3,line4,line5,line6,line7]
    
    #Print out results to terminal
    for line in lines:
        print(line)

    #text file that contains the result of the analysis
    file_path = "analysis\output.txt"
    with open(file_path, "w") as file:
        for line in lines:
            file.write(line)
            