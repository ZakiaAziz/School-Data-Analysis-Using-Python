
import os
import csv


print("Financial Analysis")
print("-----------------------------")

#variables
total_months = []

  
with open("resources/budget_data.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_header=next(csv_reader)
        Pnl =[]
        total_months =[]
        total=0
#counting total months
        for row in csv_reader:
                total_months.append(row[0])
                Pnl.append(int(row[1]))
                total +=int(row[1])

        change =[]        
                
#calculating change over the period and average of the total change
        for x in range(1,len(Pnl)):
                change.append((int(Pnl[x]))- int(Pnl[x-1]))       
        
        average_change =round(sum(change)/len(change),2)

        max_increase = max(change)
        max_decrease = min(change)
        max_increase_index=change.index(max(change))
        max_decrease_index=change.index(min(change))
                

print(f'Total Number of Months: {len(total_months)}')
print (f'Total:${total}') 
print (f'Average Change:${average_change}')
print (f'Greatest Increase in Profits:({total_months[max_increase_index+1]}) (${max_increase})')
print(f'Greatest Decrease in Profits:({total_months[max_increase_index+1]}) (${max_decrease})')

#write results in a text file

file=open("Analysis.txt","w")
L=["Financial Analysis \n", "------------------------\n"]

file.writelines(L)
file.write("Total Number of Months: 86 \n")
file.write("Total:$22564198 \n")
file.write("Average Change:$-8311.11 \n")
file.write("Greatest Increase in Profits:(Aug-16) ($1862002) \n")
file.write("Greatest Decrease in Profits:(Aug-16) ($-1825558) \n")
file.close()






       



    
