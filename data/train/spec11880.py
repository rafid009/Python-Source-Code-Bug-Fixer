import numpy as np 

def function(x):

	c9 = x
	v5 = 2
	x = 8
	paths = []
	try:
		if v5 <= 9:
			x = c9/x
			c9 = 5*c9
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if x >= 2:
			c9 = x/c9
			paths.append(3)
		else:
			c9 = c9-4
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		v5 = c9**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))