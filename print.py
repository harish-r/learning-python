your_name = "john"
your_age = 18
your_height = 150.6

# # %r - generic type
# # %s - string
# # %d - numbers
# # %f - floating points
formatter = "Your name is %s, you are %d years old, you are %f cm tall!"
print formatter % (your_name, your_age, your_height)

# Concatenate strings using + or using ,
hello = "hello,"
world = "world!"
# , concatenates with ,
print hello, world
# + contatenates as is
print hello + world

# print text multiple times
print 'hello ' * 10
print '.' * 20
