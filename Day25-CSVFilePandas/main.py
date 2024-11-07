# with open("weather_data.csv") as weather:
#     report = weather.readlines()
#     print(report)

# import csv
#
# with open("weather_data.csv") as weather:
#     report = csv.reader(weather)
#     temperature = []
#     for row in report:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

##Pandas challenge
import pandas
#
report = pandas.read_csv("weather_data.csv")
# print(report["temp"])
#
# # report_dict = report.to_dict()
# # print(report_dict)
# #
# # temp_list = report["temp"].to_list()
# # print(temp_list)
#
# avg_temp = report["temp"].mean()
# print(avg_temp)
# avg_temp = report.temp.mean()
# print(avg_temp)
#
# max_temp = report["temp"].max()
# print(max_temp)
#
# #Get Row Data
# print(report[report["day"] == "Monday"])
# print(report[report.temp == report.temp.max()])
#
monday = report[report.day == "Monday"]
print(monday.temp[0])
# print(((monday.temp[0] * 9) /5) + 32)
#
# new_dict = {
#     "students": ["name1", "name2", "name3"],
#     "scores": [50, 60, 70]
# }
#
# data_dic = pandas.DataFrame(new_dict)
# print(data_dic)
# print(data_dic.to_csv())

#Squirrle challenge

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_dict = squirrel_data.to_dict()

no_of_squirrels = pandas.DataFrame(squirrel_data)
# print(no_of_squirrels)

#1st approach
# grey_squirrels_count = len(no_of_squirrels[no_of_squirrels["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(no_of_squirrels[no_of_squirrels["Primary Fur Color"] == "cinnamon"])
# black_squirrels_count = len(no_of_squirrels[no_of_squirrels["Primary Fur Color"] == "black"])
#
# new_dict = {
#     "Fur Color": ["Gray", "cinnamon", "black"],
#     "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
#
# new_data = pandas.DataFrame(new_dict).to_csv("squirrel_count.csv")


#2nd approach

no_of_squirrels["Primary Fur Color"].value_counts().to_csv("squirrel_count.csv")
new_dict = {
    "Fur Color": no_of_squirrels["Primary Fur Color"].value_counts().keys().tolist(),
    "Count": no_of_squirrels["Primary Fur Color"].value_counts().values.tolist()
}

new_data = pandas.DataFrame(new_dict).to_csv("squirrel_count.csv")

# print(no_of_squirrels["Primary Fur Color"].value_counts().values.tolist())

# for colour in new_dict["Fur Color"]:
#     new_dict["Count"].append(no_of_squirrels[no_of_squirrels["Primary Fur Color"] == colour].count())
#
# new_data = pandas.DataFrame(new_dict)
# print(new_data)

