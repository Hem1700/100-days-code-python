import csv
import pandas

# with open('weather_data.csv') as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
    
#     print(temperature)


data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])

data_dict = data.to_dict()
print(data_dict)


temp_list = data['temp'].to_list()
print(temp_list)

mean = data['temp'].mean()
print(mean)

largest = data['temp'].max()
print(largest)
# avg = sum(temp_list)/(len(temp_list))
# print(avg)

print(data.day)


# Get data from the rows
print(data[data.day == 'Monday'])


print(data[data.temp == largest])


monday = data[data.day == 'Monday']
cel = monday['temp']
fahr = (cel * 9.0/5.0) + 32.0
print(fahr)


# Create a dataframe from scratch

data_dic = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76,56,65]
}

data = pandas.DataFrame(data_dic)
data.to_csv("new_data.csv")