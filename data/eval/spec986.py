import numpy as np 

def function(x):

	c7 = x
	r8 = 4
	paths = []
	try:
		if c7 <= 8:
			c7 = c7*5
			c7 = c7+4
			paths.append(1)
		else:
			c7 = x/c7
			c7 = c7/5
			paths.append(2)
		if c7 >= 2:
			r8 = 3/4
			x = x+4
			paths.append(3)
		else:
			x = x*6
			x = x+5
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))