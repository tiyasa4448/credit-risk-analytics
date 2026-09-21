text = "Vision Aid"

# # String Slicing
# # text[start : end]
# print(text[1:3])
# print(text[0:4])
# print(text[:4])
# print(text[0:])
# print(text[5:])
# print(text[:])
# print(text[4:1])
# print(text[0:20])


# # print(text[-2:-6]) # No Output, 'start' > 'end'
# # use the syntax text[start : end : step]
# print(text[-2:-7:-1]) # -1 is the step (increment)
# print(text[0:10:2]) # prints alternate characters between index 0 and index 10 (exclusive)

# print("Qaderoon"[3:])
# name = "Qaderoon"
# print(name[3:])


# # Strings are Immutable
# text[4] = ","
# print(text)
# text = text[0:4] + "," + text[5:]
# print(text)


# # The 'in' operator
# print('e' in text)
# print('a' in text)
# print("ome" in text)


# # print(1 in 123) # TypeError
# print("1" in "123")
# print(str(1) in str(123))


# # String comparison
# print("Shyam" == "shyam")
# print("He" > "She")