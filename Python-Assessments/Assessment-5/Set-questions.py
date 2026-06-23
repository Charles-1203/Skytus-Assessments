# Create a tuple with 5 numbers.

tup1=(1, 2, 3, 4, 5)
print(tup1)

# Access the third element in a tuple.

print(tup1[2])

# Unpack a tuple into separate variables.

tup2=("Charles",21,"IT")
name,age,department=tup2
print(name)
print(age)
print(department)


# Create a set of 5 fruits.

tup3={"Apple", "Banana", "Cherry", "Mango", "Grapes"}

print(tup3)

# Add a new fruit to the set.

tup3.add("Orange")
print(tup3)
# Remove an element from a set.
tup3.remove("Banana")
print(tup3)

# Find union of two sets.

tup3={"Apple", "Banana", "Cherry", "Mango", "Grapes"}
tup4={"Pineapple", "Strawberry", "Watermelon", "Mango", "Grapes"}   

union_set=tup3.union(tup4)
print(union_set)

# Find intersection of two sets.

intersection_set=tup3.intersection(tup4)
print(intersection_set)

# Check if one set is subset of another.

check=tup3.issubset(tup4)
print(check)

# Convert a list with duplicate values into a set to remove duplicates.

list1=[1, 2, 3, 4, 5, 2, 3, 1]
set1=set(list1)
print(set1)
