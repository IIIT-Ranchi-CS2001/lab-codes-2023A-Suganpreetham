import pandas as pd
import csv

#(Question 1) first 5 rows 
print("The first 5 rows are:")
with open("AQI_Data.csv", mode="r") as file:
    reader = csv.reader(file)
    # Printing first 5 rows
    for i, row in enumerate(reader):
        if(i<5):
            print(row)
        else:
            break

#(Question 2) last 6 rows
print("The last 6 rows are:")
with open("AQI_Data.csv", mode="r") as file:
    reader = csv.reader(file)
    rows = list(reader)  
    #printing last 6 rows
    for row in rows[-6:]:
        print(row)

# (Question-3) Summary Statistics
filepath = 'AQI_Data.csv'
data = pd.read_csv(filepath)
# Printing summary statistics
SummaryStatics = data.describe()
print("Summary Statistics for all Numeric Columns:")
print(SummaryStatics)

# (Question-4) Calculating the mean 
MeanOfThree = data[['AQI', 'PM2.5', 'PM10']].mean()
# Printing mean
print("Mean values of three columns:")
print(f"AQI: {MeanOfThree['AQI']}")
print(f"PM2.5: {MeanOfThree['PM2.5']}")
print(f"PM10: {MeanOfThree['PM10']}")

# SET-1(Private question)
City_Avg_AQI = data.groupby('City')['AQI'].mean()
# Calculating lowest and highest avg AQI cities without using idxmax() and idxmin()
# Converting the result to a dictionary
city_avg_aqi_dict = City_Avg_AQI.to_dict()

# Find the city with the lowest and highest average AQI using the dictionary
lowest_aqi_city = min(city_avg_aqi_dict, key=city_avg_aqi_dict.get)
highest_aqi_city = max(city_avg_aqi_dict, key=city_avg_aqi_dict.get)

print(f"City with the lowest average AQI: {lowest_aqi_city} ({city_avg_aqi_dict[lowest_aqi_city]})")
print(f"City with the highest average AQI: {highest_aqi_city} ({city_avg_aqi_dict[highest_aqi_city]})")