# iteration trough lists

#1 Way for each loop is simple, modification of list not possible

my_list = [1, 3, 4, 2]
for item in my_list:
    print(item)


print()
#2 Way acces by index, modification of list is possible

for i in range(len(my_list)):
    print(my_list[i])

# adding to a list
my_list.append(9)
print(my_list)

# Creating a list from user input
# my_list = []
# for i in range(3):
#     user_input = input("Enter an integer: ")
#     user_input = int(user_input)
#     my_list.append(user_input)
#     print(my_list)

# create a list with 100 zeros
my_list = [0] * 100
print(my_list)

# summing a list
my_list = [5, 5, 80, 3, 4, 5]
list_total = 0
for i in range(len(my_list)):
    list_total += my_list[i]
print(list_total)

#or

my_list = [3, 3, 3, 3, 3]
list_total = 0
for item in my_list:
    list_total += item
print(list_total)

# doubling all numbers in list, only works with direct access by index
# not by copying the list items like "for item in my_list"
for i in range(len(my_list)):
    my_list[i] *= 2
print(my_list)

# doesn't work because only double the copy of the item
# for item in my_list:
#     item *= 2
# print(my_list)

#x = "This is a sample string"
x = "0123456789"

# Accessing a single character
print("x[0] = ", x[0])
print("x[1] = ", x[1])

# Accessing from right side
print("x[-1] = ", x[-1])

# Access index 0-5
print("x[:6] = ", x[:6])

# Access 6 to end
print("x[6:] = ", x[6:])

# Access  index 5-8
print("x[5:9] = ", x[5:9])

# adding and multiplying strings
a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

for character in "This is a test.":
    print(character)

# # exercise
# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# for i in range(5):
#     n = int(input("Enter a month number: "))
#     print(months[n * 3 - 3 : 3 * n])

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=" ")

print()

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=" ")

print()

# encrypting with utf-8

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")

print()

# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Explanation video: http://youtu.be/sxFIxD8Gd3A

plain_text = "This is a test. ABC abc"

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

# get the average of a list
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
list_total = 0
for i in range(len(my_list)):
    list_total += my_list[i]
print(list_total / len(my_list))
