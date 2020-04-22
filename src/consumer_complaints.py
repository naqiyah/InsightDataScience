
#importing the csv file 
from collections import Counter,OrderedDict 
import math
import csv  
file =  open('../input/complaints.csv', 'r')
reader = csv.reader(file)

items = []  # put the rows in csv to a list
Date_Product = []  # to have a tuple of aisle and dept ids
mydict = {} # product as keys and list of above tuple as values in a dictionary

Date, product, company, timestam = [],[],[],[]

for row in reader:
   items.append(row)

#seperating the columns pushing them into tuples
for i  in range(1, len(items)):
    Date.append(items[i][0].lower())
    product.append(items[i][1].lower())
    company.append(items[i][7].lower())


#print(Date)
#print(product)
#print(company)

#seperating the year from the date 
from datetime import datetime

for i in range(0, len(Date)):
    my_string = Date[i]
    my_date = datetime.strptime(my_string, "%Y-%m-%d")
    my_year = my_date.year
    timestam.append(my_year)
print(timestam)


#Capturing the required main categories in the tuple
for item1, item2,item3 in zip(timestam,product,company):
    Date_Product.append((item2, item1,item3))

print(Date_Product)

#Forming the dictionaries 
for x in Date_Product:
    if x[0] in mydict.keys():
        if x[1] in mydict[x[0]].keys(): 
            mydict[x[0]][x[1]].append(x[2])
        else:
            company_list= [x[2]]
            mydict[x[0]][x[1]] = company_list
        
    else:
        year_dict = dict()
        company_list = [x[2]]
        year_dict[x[1]] = company_list
        mydict[x[0]] = year_dict
        
print(mydict) 


a_file = open("../output/report.csv", "w")
mydict = OrderedDict(sorted(mydict.items())) 
print(mydict)
writer = csv.writer(a_file)
for product_name, year_dict in mydict.items():
#year,no_of_complaints, no_of_companies
    year_dict = OrderedDict(sorted(year_dict.items()))
    for year,company_list in year_dict.items():
        no_of_complaints = len(company_list)
#no_of_companies = len(set(company_list))
        companydict = Counter(company_list)
        no_of_companies = len(companydict)
        percentage = math.ceil(max(companydict.values())/no_of_complaints*100)
        writer.writerow([product_name,year,no_of_complaints,no_of_companies,percentage])

a_file.close()
