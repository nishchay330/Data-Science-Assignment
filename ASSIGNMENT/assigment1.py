# QUESTION 1
name="nishchay"
print(name[0])
print(name[7])
print(len(name))
print(name.upper())
print(name.lower())
print( name[::-1])

# QUESTION 2
car="mercedes"
print(car[0:5])
print(car[2:5])
print(car[::-1])

# QUESTION 3
lst=[1,2,3,4]
lst.append(5)
print(lst)
lst.insert(2,8)
print(lst)
lst.remove(3)
print(lst)
lst.pop(1)
print(lst)
print(lst[::-1])
lst.sort()
print(lst)
print(len(lst))
print(lst.count(4))

# QUESTION 4
tpl=(1,2,2,4,5)
print(len(tpl))
print(tpl[0])
print(tpl[-1])
print(tpl[0:4])
print(max(tpl))
print(min(tpl))
print(sum(tpl))

# QUESTION 5
tpl=(13,7,"hello") #tuple packing
print(tpl)
a,b,c=(13,7,"hello")  #tuple unpacking
print(a)
print(b)
print(c)

# QUESTION 6
dict={"name":"nishchay","age":"21","course":"BTECH","address":"jaipur"}
print(dict.keys())
print(dict.values())
print(dict.items())
dict["address"]="kota"
print(dict)
dict["branch"]="CS(AI)"
print(dict)

# QUESTION 7
lst=[1,2,3,4,[2,5],7]
print(lst[4][1])

# QUESTUION 8
num=int(input("enter the value"))
num+=10
print(num)

# QUESTION 9
num1=int(input("enter the value1"))
num2=int(input("enter the value2"))
num3=num1*num2
print(num3)

# QUESTION 10
dict={"name":"nishchay","age":"21","course":"BTECH","address":"jaipur"}
print(dict.get('name'))  #used to get the value
print(dict.keys())  #used to get the keys
print(dict.values())  #used to get the values
print(dict.items())  #used to get all the items in the dictionary

# QUESTION 11
list1 = [10, 20, 30, 40, 50]
list2 = list1.copy()
print("Original List:", list1)
print("Copied List:", list2)
