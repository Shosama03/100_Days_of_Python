import pandas
# data = pandas.read_csv(r"./Day_25/weather_data.csv")
# print(type(data))
# print(data["condition"]) 

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# maxm = data["temp"].max()
# print(data.condition)

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#Creating a dataframe from scratch
# data_dict = {
#     "students":["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv(r"./Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260205.csv")
# print(data)

fur_color = ["grey","red","black"]
grey_count = len(data[data["Primary Fur Color"] == "Gray"]) 
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"]) 
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":fur_color,
    "Count":[grey_count,red_count,black_count]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv(r"./Day_25/squirrel_count.csv")
