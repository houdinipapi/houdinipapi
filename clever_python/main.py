#!/usr/bin/python3
user_input = input()
user_input = user_input.replace(" ", "***")
print(user_input)

name_list = ["Papi", "Chulo", "Houdini"]
for i in name_list:
    if name_list[i] == "Chulo":
        name_list[i] = i.replace("Chulo", "Huncho")
print(name_list)
