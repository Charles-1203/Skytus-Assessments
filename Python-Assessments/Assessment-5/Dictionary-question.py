    
# Create a dictionary storing student names and marks.

dic1={
    "name":"Charles",
    "marks": 7.8
}
print(dic1)

# Add a new key-value pair to an existing dictionary.

dic1["age"]=21
print(dic1) 

# Delete a key-value pair from a dictionary.

print(dic1.pop("marks"))
print(dic1)

# Merge two dictionaries into one.

dic2={
    "department":"IT", 
    "name":"tirth"}


print({**dic1, **dic2})

# Check if a key exists in a dictionary.

if "name" in dic1:
    print("Key exists in the dictionary.")
else:    
    print("Key does not exist in the dictionary.")


# Count word frequency in a given string using a dictionary.

text="Hi , My name is Charles and I am a student in IT department. I am 21 years old."
word_freq={}
for word in text.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)


# Find the key with the maximum value in a dictionary.


max_key=max(dic1, key=dic1.get)
print("Key with maximum value:", max_key)

# Reverse keys and values in a dictionary.

reversed_dic={value: key for key, value in dic1.items()}
print(reversed_dic)

# Update the value for a specific key.

dic1["age"]=22
print(dic1)

# Convert a list of tuples into a dictionary.

tup7=[("name", "Charles"), ("age", 21), ("department", "IT")]
dic3=dict(tup7)
print(dic3)