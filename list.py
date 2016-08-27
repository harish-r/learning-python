# Learning Python
# learning lists in python 2.7

# Empty list. Create using []
empty_list = []
# list can have items of same data type
uni_list = [1, 2, 3, 4, 5]
# list can have items of different data type
multi_list = ['hello', 24, 56.80, "world", False]

# Accessing list items (and slicing)
print uni_list[1]			# Index starts from zero
print uni_list				# Prints the whole list
print uni_list[0:4]			# from index m to n-1
print uni_list[1:]			# from index 1 to end of list
print uni_list[:2]			# from beginning to index n-1

# Looping though list items
for item in uni_list:
	print item * 2
for item in multi_list:
	print item

# List operations
alp_list = ['a', 'b', 'c', 'd']
# + Concatenates two lists
new_list = alp_list + uni_list
print new_list
# * expands list into n times same list
expand_list = alp_list * 2;
print expand_list

# append(item) adds item to the end of list
alp_list.append('d')

# pop(index) removes element at the index
# no index deletes the last element
deleted_item = alp_list.pop()
# remove(element) deletes the element 
alp_list.remove('c')
# del list[index] deletes the element at the index
del alp_list[2]
alp_list.append('e')
alp_list.append('d')
# count(item) returns the number of occurances of item
print alp_list.count('e')

nums = [3, 41, 12, 9, 74, 15] 
# List math operations
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
# sort() sorts the list
nums.sort()
print nums
# reverse() reverses the list
nums.reverse()
print nums

s = "hello world. I am your program"
# convert string to list of characters
chars = list(s)
print chars
# split a string into words
words = s.split()
print words

# End of file