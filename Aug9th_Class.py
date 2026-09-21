#Topic 1: Creating a string, and axising individual characters of the string.

greeting = "Hello world"

# print(type(greeting))
# print(greeting)

#fullname = input("Enter your full name: ")
## print(fullname)
# print(type(fullname))

# letter = greeting[0]
# print(letter)
# print(type(letter))
# print(greeting[6])

#print(greeting[10])
#print(greeting[-1])
#print(fullname[len(fullname)-1])
#print(fullname[-1])

#Topic 2: Traversing a string.

#for char in greeting:
#    print(char)

# for char in range(len(greeting)):
#     print(char)
#     print(greeting[char])

# i = 0
# while i < len(greeting):
#     print(greeting[i])
#     i +=1

#Topic 3: String slicing

# substr = greeting[0:2]
# print(substr)
# print(greeting[6:9])

# print(greeting[:5])
# print(greeting[6:])
# print(greeting[:])
# print(greeting[0:len(greeting):2])

#Topic 4: Strings are immutable

greeting[1] = "a"