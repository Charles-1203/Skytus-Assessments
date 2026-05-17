# Take a string input and print its length.


str=input("Enter a string: ")

print("length of the string is: ",len(str))


# Convert a sentence to lowercase.

str1="HELLO WORLD"
print(str1.lower())



# Replace spaces with underscores in a string.

str3="Hello World"   

print(str3.replace(" ","_"))




# Extract the first and last character of a string.

str4="Charles"

print("First character: ",str4[0])
print("Last character: ",str4[-1])



# Reverse a string using slicing.

str5="Patel"

print("Reversed string: ",str5[::-1])



# Count how many times a letter appears in a string.

str6="skytus python course"

print("Number of times 'y' appears: ",str6.count('y'))






# Check if a word is present in a sentence.

str7="Collect your offer letter from portal."

word="offer"
if word in str7:

    print(word,"is present in the sentence.")

else:
    print(word,"is not present in the sentence.")




# Take name & age and print using f-string formatting.

name=input("Enter your name: ")
age=int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

# Remove extra spaces from the start and end of a string.

str8=" hello kem cho  "   

print("String after removing extra spaces:",str8.strip(),"Original string:",str8)



# Join a list of words into a single string with - between them.


words=["Hello","World","Python"]

joined_string="-".join(words)
print("Joined string:",joined_string)
