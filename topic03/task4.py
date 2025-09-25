list=["apartment", "banana", "cherry"]
a="car"
b="zoo"
def add_to_list(list, item):
    for i in range(len(list)):
       if item < list[i]:
        return i
       else:
        continue
    return len(list)
   
list.insert(add_to_list(list, a), a)
print(list)

list.insert(add_to_list(list, b), b)
print(list)