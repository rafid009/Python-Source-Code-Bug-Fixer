import numpy as np 

def function(x):

	c8 = x
	i9 = x
	paths = []
	try:
		if i9 < 7:
			i9 = 0-1
			paths.append(1)
		else:
			x = x*c8
			c8 = c8*0
			paths.append(2)
		if x <= 9:
			i9 = i9-i9
			c8 = c8*1
			paths.append(3)
		else:
			i9 = 7-i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))