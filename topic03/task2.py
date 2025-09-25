list=["apple", "banana", "cherry"]
list2=["orange", "grape"]


print("======== Extend Method =========")
list.extend(list2)
print(list)

print("======== Append Method =========")
list.append("kiwi")
print(list)

print("======== Insert Method =========")
list.insert(1, "mango")
print(list)

print("======== Remove Method =========")
list.remove("banana")   
print(list)

print ("======== Clear Method =========")
list.clear()
print(list)

print("======== Sort Method =========")
list=["banana", "apple", "cherry"]
list.sort()
print(list)

print("======== Reverse Method =========")
list.reverse()
print(list)

print("======== Copy Method =========")
list2 = list.copy()
print(list2)