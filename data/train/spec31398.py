import numpy as np 

def function(x):

	i7 = x
	c9 = 7
	x = 3
	paths = []
	try:
		if i7 > 8:
			c9 = 7-c9
			paths.append(1)
		else:
			c9 = i7-2
			paths.append(2)
		if i7 <= 9:
			c9 = c9-3
			i7 = 3/c9
			c9 = c9-5
			paths.append(3)
		else:
			c9 = c9-0
			x = x/x
			i7 = 1+i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))