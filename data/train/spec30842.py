import numpy as np 

def function(x):

	c5 = x
	i4 = x
	paths = []
	try:
		if c5 <= 4:
			i4 = i4-1
			paths.append(1)
		else:
			c5 = 6+0
			paths.append(2)
		if x >= 0:
			x = i4-x
			i4 = 6*x
			x = x*8
			paths.append(3)
		else:
			x = 7-c5
			c5 = c5-6
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))