import numpy as np 

def function(x):

	r3 = x
	c9 = x
	paths = []
	try:
		if c9 >= 7:
			c9 = c9-6
			paths.append(1)
		else:
			c9 = c9-6
			paths.append(2)
		if c9 >= 2:
			r3 = r3+x
			x = x*6
			paths.append(3)
		else:
			c9 = c9*c9
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))