import numpy as np

covid_data = np.array([ 
[1500, 2000, 1800, 1200, 900 ],     # Day 1 
[1600, 2100, 1900, 1300, 950 ], 	# Day 2 
[1700, 2200, 2000, 1400, 1000], 	# Day 3 
[1650, 2150, 1950, 1350, 980 ], 	# Day 4 
[1750, 2250, 2050, 1450, 1020], 	# Day 5 
[1800, 2300, 2100, 1500, 1050], 	# Day 6 
[1900, 2400, 2200, 1600, 1100], 	# Day 7 
])
total_cases_percountry=[]
for i in range(0,5):
    sum=int(0)
    for j in range(0,7):
        sum=sum+covid_data[j][i]
    total_cases_percountry.append(int(sum))

country=['Country_A','Country_B','Country_C','Country_D','Country_E']
total_cases=zip(country,total_cases_percountry)
total_cases=list(total_cases)
print("total cases in each country are: ",total_cases)
print("The country with highest cases are:",max(total_cases, key=lambda x: x[1] ))

#avg cases across all countries per day
total_cases_perday=[]
avg_cases_perday=[]

for i in range(0,7):
    sum=int(0)
    for j in range(0,5):
        sum=sum+covid_data[i][j]
    total_cases_perday.append(int(sum))
    avg_cases_perday.append(int(sum)/5)

print("Average cases per day across all countries are:",avg_cases_perday)
print("The day with the highest total number of cases across all countries:",total_cases_perday.index(max(total_cases_perday))+1)
percentage_incordec=[]
for i in range(0,5):
    z=int(((covid_data[6][i]/covid_data[0][i])*100)%100)
    percentage_incordec.append(int(z))
print("The percentage increase or decrease from day 1 to 7:",percentage_incordec)
highest_inc_index=percentage_incordec.index(max(percentage_incordec))
print(f"The highest percentage increase country is {country[highest_inc_index]} that is :{percentage_incordec[highest_inc_index]}%")