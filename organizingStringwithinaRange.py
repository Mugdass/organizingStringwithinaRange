

"""Problem 1"""



names_of_months=["January","February","March","April","May","June","July","August","September","October","November","December"]
print(names_of_months)







"""Problem 2"""


for x in range(0,12):
    print(str(x+1)+" "+names_of_months[x])


for x in range(0,12):
    print(str(x+1)+". "+names_of_months[x])
    

for x in range(12):
    print(str(x+1)+") "+names_of_months[x])
    


for x in range(0,12):
    print(str(x+1)+") "+names_of_months[x])
    



for x in range(0,12):
    print("Month " + str(x+1)+" is "+names_of_months[x])
