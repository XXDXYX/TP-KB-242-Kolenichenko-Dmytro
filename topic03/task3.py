

my_dict ={"a": 1, "b": 2, "c": 3}

print("======== Update Method =========")
my_dict.update({"b": 3, "d" : 4})
print(my_dict)

print("======== Del Method =========")
del my_dict["a"]
print(my_dict)

print("======== Clear Method =========")
my_dict.clear()
print(my_dict)

print("======== Keys Method =========")
my_dict ={"a": 1, "b": 2, "c": 3}
print(my_dict.keys())

print("======== Values Method =========")
print(my_dict.values())

print("======== Items Method =========")
print(my_dict.items())