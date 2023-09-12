# CSCI 372
# Assignment 1, Question 2
# Write a small script to check if two strings have the same id if they have the same
# value, if a list keeps its id when it changes, and other findings.


# Experimentation with String memory location
# When two string objects have been initialized as the same arrangement of characters,
# they are set to the same memory location. However, if two string objects are initialized
# differently, they are set to different locations. Even if one is concatenated to equal
# the other using the '==' operator, they will keep their individual locations.
stringA = "Hello"
stringB = "Hello"
stringC = "Hell"
stringC += "o"

# Show that the strings have the same value
if stringA == stringB:
    print("stringA (" + stringA + ") has the same value as stringB (" + stringB + ")")
else:
    print("stringA (" + stringA + ") has a different value from stringB (" + stringB + ")")
if stringA == stringC:
    print("stringA (" + stringA + ") has the same value as stringC (" + stringC + ")")
else:
    print("stringA (" + stringA + ") has a different value from stringC (" + stringC + ")")

# Show that A and B have the same ID, but C has another ID
if id(stringA) == id(stringB):
    print("stringA and stringB have the same ID: " + str(id(stringA)))
else:
    print("stringA and stringB have different IDs.")
if id(stringA) == id(stringC):
    print("stringA and stringC have the same ID: " + str(id(stringA)))
else:
    print("stringA and stringC have different IDs. While stringA " +
          "was initialized as 'Hello', stringC was initialized as a " +
          "different value, then concatenated to 'Hello'.\n")
    

# Experimentation with list memory locations
# A list will keep its memory location when objects are added to it.
listA = list()
print("listA starts with out as empty as has the ID: " + str(id(listA)) + ".")
id1 = id(listA)
listA += stringA
if id1 == id(listA):
    print("After stringA is added to listA, its ID is: " + str(id(listA)) + 
        ". Therefore, changing the contents of a list does not change its id.\n")
else:
    print("After stringA is added to listA, its ID is: " + str(id(listA)) +
          ". Therefore, changing the contents of a list changes its memory location.\n")


# Experimentation with integers
# Like strings, integers initialized with the same value have the same memory location.
# However, when operatons are performed on integers, the script will try to assign it
# to an existing integer variable's memory location to save space.
num0 = 0
num1 = 1
print("num0 and num1 have been initialized to 0 and 1 respectively. Their ids are " +
      "different. num0's id is: " + str(id(num0)) + ", and num1's: " + str(id(num1)) + ".")
num1 = 0
print("Now that num1 has been set to 0, its id is: " + str(id(num1)) + ". Its memory " +
      "location has now been set to num0's.")
num1 = 1
num1 -= 1
print("num1 was set back to 1 and was decremented by 1. Its id is: " + str(id(num1)) + ". Its memory " +
      "location has now been set to num0's even though it wasn't explicitly set to 0.")