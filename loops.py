# Range function, 0 - n-1 numbers
for i in range(10):
	print i,
print '\n'

# Range function m to n-1 numbers
for i in range (1, 11):
	print i,
print '\n'

alphabets = ['a', 'b', 'c', 'd', 'e']
for alphabet in alphabets:
	print alphabet,
print '\n'

# While loop: executes until the condition is true
# while condition:
n = 5
while n >= 0:
	print n
	n = n - 1

# While loop with break
n = 5
while True:
	print n
	n = n - 1
	if n == 0:
 		break
print "End"