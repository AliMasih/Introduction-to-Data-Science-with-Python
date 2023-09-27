myList = ["Ali", "Ali",  "Laila", "Maryam", "Mahdi"]
print(myList)
print(len(myList))

# list utem data type

list1 = ["Ali", "Aziza", "Mahdi"]
print(type(myList))
list2 = [2, 4, 6, 8, 10]
list3 = [True, False, False, False, True]

list4 = ["Ali", True, 1234, "Masih"]
# Access item in list
print(list4[2])

# list negative indexing
listD = ["Ali", "Laila", "Mustafa", "Maryam", "Baran"]
print(listD[-1])

# range of index 
fruits = ["Apple", "Banana", "Cherry", "Mango", "Kiwi", "Melon"]
print(fruits[2:4])
print(fruits[:3])
print(fruits[4:])

# Change item Value
listD = ["apple","banana", "cheryy"]
listf = ["mango", "berry", "apricote"]
listD.extend(listf) # c
listD[1] = "kiwi"
print(listD)

# Changing range of item values
score = [20, 29, 30,23, 28, 30, 19]
score.insert(3, 35) # insert an item to list
score.append(17) # add item to the end of list
score.remove(29) # removing the element
print(score)
score[2:5] = [18, 21, 24] # replace item in list
print(score)
