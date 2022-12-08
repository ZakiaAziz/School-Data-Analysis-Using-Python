# python challenge
 
with open("/Users/zakiaafrinaziz/Desktop/python-challenge/PyBank/resources/budget_data.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_header=next(csv_reader)
        total=0
        change=0
        average_change=[]

        for row in csv_reader:
                total_months.append(row[0])
                total +=int(row[1])
                for row in csv_reader:
                        change=row[1]

        print(f'Total Number of Months: {len(total_months)}')
        print (f'Total:${total}') 
        print(average_change)

       