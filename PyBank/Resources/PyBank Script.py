#import modules
import os, csv

#C:\Users\tatia\OneDrive\Desktop\Rutgers Bootcamp Repository\python-challenge\PyBank\Resources
#terminal needs to be in the same folder as the python file
#open csv file and create dictionary using the columns in the dataset
with open('budget_data.csv', "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        data = list(reader)        

#print(data)

#set variables
tot_rev = 0
greatest_inc = 0
greatest_inc_mo = ""
greatest_dec = 0
greatest_dec_mo = ""
prev_rev = 0
change = []

#use a loop to go through all the data
for row in data:
        date = row[0]
        revenue = int(row[1])
#The net total amount of "Profit/Losses" over the entire period
        tot_rev += revenue
        change.append(int(row[1]) - prev_rev)
        prev_rev = revenue


#The total number of months included in the dataset
months = len(data)

print(months)
print(tot_rev)


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
average = round((int(data[-1][1]) - int(data[0][1])) / (months - 1), 2)
print(average)

#The greatest increase in profits (date and amount) over the entire period
for n in range(1, len(change)):
        if change[n] > greatest_inc:
                        greatest_inc = change[n]
                        greatest_inc_mo = data[n][0]
#The greatest decrease in profits (date and amount) over the entire period                     
        if change[n] < greatest_dec:
                greatest_dec = change[n]
                greatest_dec_mo = data[n][0]

print(f'{greatest_inc_mo}, ${greatest_inc}, {greatest_dec_mo}, ${greatest_dec}')

#print Financial Analysis sheet
print()
with open("Financial Analysis.txt", "w") as file_PythonChallenge:
        file_PythonChallenge.write(f"""Financial Analysis
-----------------------------
Total months: {months}
Total: {tot_rev}
Average Change: ${round(average, 2)}
Greatest Increase in Profits: {greatest_inc_mo} (${greatest_inc})
Greatest Decrease in Profits: {greatest_dec_mo} (${greatest_dec})""")

