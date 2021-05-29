import numpy as np 

def function(x):

	i5 = 2
	c8 = x
	paths = []
	try:
		if i5 >= 6:
			c8 = 6*x
			i5 = 8/i5
			paths.append(1)
		else:
			x = x*6
			c8 = c8+7
			i5 = c8+7
			paths.append(2)
		if c8 > 5:
			i5 = i5-3
			x = x+8
			paths.append(3)
		else:
			i5 = 7*i5
			x = x/x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))