import numpy as np 

def function(x):

	i7 = 3
	c8 = x
	paths = []
	try:
		if i7 > 7:
			i7 = i7+6
			x = 8-i7
			paths.append(1)
		else:
			c8 = 6-5
			i7 = x+i7
			paths.append(2)
		if x <= 7:
			c8 = c8-5
			c8 = c8*i7
			paths.append(3)
		else:
			x = 7-x
			c8 = 9/c8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))