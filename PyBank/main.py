# import the os module
import os
import csv

# set path for csv file
bank_csv = os.path.join("budget_data.csv")

# read the csv file
with open (bank_csv, 'r') as csvfile:
    # split the data
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header
    next(csvreader, None)

    # assign  variables and set to 0 
    Months_Count = 0 
    Total_Profit = 0
    Greatest_Increase = 0
    Greatest_Decrease = 0
    initial_profit = 0

    # set the list to store data
    monthly_changes = []
    profit = []
    date = []

    
    # loop through data
    for row in csvreader:

        # calculate the total number of months
        Months_Count = Months_Count + 1
    
        # for greatest increase/deacrease
        date.append(row[0])

        # calculate the total profit 
        profit.append(row[1])
        Total_Profit = Total_Profit + int(row[1])
        

        # calculate the changes from month to month
        final_profit = int(row[1])
        monthly_change_profit = final_profit - initial_profit

        # add the calculation result to the list 
        monthly_changes.append(monthly_change_profit) 


        # calculate the average change in profit
        Avg_Profit_Change = sum(monthly_changes)/len(monthly_changes)

        # reduce result by 2 decimals
        Avg_Profit_Change = float('%.2f'%(Avg_Profit_Change))

        # calculate the Greatest Profits/Losses Increase/Deacrease 
        Greatest_Increase = max(monthly_changes)
        Greatest_Decrease = min(monthly_changes)

        increase_date = date[monthly_changes.index(Greatest_Increase)]
        decrease_date = date[monthly_changes.index(Greatest_Decrease)]

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(Months_Count))    
    print("Total Profits: " + "$" + str(Total_Profit))
    print("Average Change: " + "$" + str(int(Avg_Profit_Change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(Greatest_Increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(Greatest_Decrease) + ")")

#  write text doc with results     
with open('finacial_analysis.txt', 'w') as text:
    text.write("---------------------------\n")
    text.write("    Financial Analysis" + "\n")
    text.write("---------------------------\n\n")
    text.write(     "Total Months: " + str(Months_Count) + "\n")    
    text.write(     "Total Profits: " + "$" + str(Total_Profit) + "\n")
    text.write(     "Average Change: " + "$" + str(int(Avg_Profit_Change)) + "\n")
    text.write(     "Greatest Increase in Profits: " + str(increase_date) + " ($" + str(Greatest_Increase) + ")\n")
    text.write(     "Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(Greatest_Decrease) + ")\n")
    text.write("---------------------------\n")
 







        
        
        
        
      
    
                      
    



        





    



    









