my_dict = {
    "Name" : "Jabbar",
    "Salary" : 100000,
    "City" : "Karachi",
    "Profession" : "AI Developer"
}

new_dict = {"Country" : "Pakistan"}
my_dict.update(new_dict)
print(my_dict)


my_dict.pop("City")
print(my_dict)


