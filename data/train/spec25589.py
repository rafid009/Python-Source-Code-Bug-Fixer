import numpy as np 

def function(x):

	c8 = 3
	i7 = x
	paths = []
	try:
		if c8 > 7:
			c8 = c8-0
			i7 = i7*0
			paths.append(1)
		else:
			x = x+6
			x = 8-x
			paths.append(2)
		if c8 < 3:
			x = i7+i7
			c8 = c8-3
			paths.append(3)
		else:
			c8 = c8-c8
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