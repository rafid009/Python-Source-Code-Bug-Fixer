import numpy as np 

def function(x):

	c9 = x
	o8 = x
	paths = []
	try:
		if o8 < 3:
			c9 = c9+5
			paths.append(1)
		else:
			c9 = c9-o8
			x = x-x
			x = x+o8
			paths.append(2)
		if x <= 3:
			x = 0+x
			paths.append(3)
		else:
			x = 8*5
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		o8 = c9**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))