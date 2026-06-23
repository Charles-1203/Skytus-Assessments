# Create a list of your 5 favorite movies.

favorite_movies = ["Taare Zameen par", "Money Heist", "Squid Game", "Bahubali", "Stranger Things"]

print("My favorite movies are: ",favorite_movies)

# Add a new movie to the list.

new_movie="Misiion Mangal"

favorite_movies.append(new_movie)
print("Updated list of favorite movies: ",favorite_movies)


# Remove the first movie from the list.

favorite_movies.pop(0)
print("List after removing the first movie: ",favorite_movies)



# Sort a list of numbers in ascending order.


numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted numbers: ",numbers)



# Reverse a list.
numbers.reverse()
print("Reversed numbers: ",numbers)     


# Find the largest number in a list.

largest_number = max(numbers)
print("Largest number: ",largest_number)

# Merge two lists into one.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list: ",merged_list)

# Access the last element of a list without using index number.

last_element = merged_list.pop()
print("Last element of the merged list: ",last_element)

# Create a nested list and access a specific inner element.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
inner_element = nested_list[1][2]
print("Accessed inner element: ",inner_element) 
# Count how many times an element appears in a list.

occurance=merged_list.count(5)
print("Number of times 5 appears in the merged list: ",occurance)


 