import numpy as np 

def function(x):

	p4 = x
	i9 = 2
	paths = []
	try:
		if i9 <= 1:
			x = i9-3
			paths.append(1)
		else:
			i9 = x-i9
			paths.append(2)
		if i9 >= 9:
			p4 = 7*p4
			x = 0/i9
			x = 0-x
			paths.append(3)
		else:
			p4 = i9/p4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))