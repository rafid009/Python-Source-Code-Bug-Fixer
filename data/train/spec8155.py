import numpy as np 

def function(x):

	c2 = x
	i2 = 7
	paths = []
	try:
		if i2 < 9:
			i2 = i2*6
			c2 = c2-x
			x = x/i2
			paths.append(1)
		else:
			c2 = c2/9
			x = x-c2
			paths.append(2)
		if x <= 6:
			x = 1-x
			paths.append(3)
		else:
			i2 = 7*i2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))