import numpy as np 

def function(x):

	o6 = x
	c0 = x
	paths = []
	try:
		if x > 4:
			o6 = 3*8
			paths.append(1)
		else:
			c0 = x-o6
			paths.append(2)
		if c0 >= 4:
			x = 5+1
			c0 = c0-8
			paths.append(3)
		else:
			x = 9-0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))