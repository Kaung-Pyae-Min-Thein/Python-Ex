# with open("weather_data.csv") as file:
#         data = file.readlines()
# print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#         data = csv.reader(data_file)
#         temperature = []
#         # new_temp = []
#         # for row in data:
#         #         temperature.append(row[1])
#         # print(temperature)
#         # for i in temperature[1:]:
#         #         new_temp.append(int(i))
#         # print(new_temp)
#         for row in data:
#                 if row[1] != "temp":
#                         temperature.append(int(row[1]))
#         print(temperature)
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(temp_list)
# maximum =data['temp'].max()
# print(maximum)
# total_temp = 0
# for one_temp_list in temp_list:
#         total_temp += one_temp_list
# avg_temp = total_temp/ len(temp_list)
# avg_temp = sum(temp_list)/ len(temp_list)
# print(avg_temp)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp)
# import pandas
#
# data_dict = {
#         "students": ["Amy", "James", "Angela"],
#         "scores": [60,35, 34]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
import pandas

# gray = 0
# red = 0
# black = 0
data = pandas.read_csv("Squirrel_Data.csv")
# find squirrel color count
# fur_color_list = data["Primary Fur Color"].to_list()
# for color in fur_color_list:
#         if color == "Gray":
#                 gray += 1
#         elif color == "Cinnamon":
#                 red += 1
#         elif color == "Black":
#                 black += 1
# another way
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

# create new DataFrame and export CSV
data_dict = {
        "Fur Color": ["Grey", "Red", "Black"],
        # "Count": [gray, red, black]
        "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
squirrel_dataframe = pandas.DataFrame(data_dict)
squirrel_dataframe.to_csv("squirrel_count.csv")


