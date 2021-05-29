import numpy as np 

def function(x):

	c3 = 0
	r8 = x
	paths = []
	try:
		if x >= 6:
			x = x-7
			x = 2*6
			paths.append(1)
		else:
			c3 = 4+c3
			paths.append(2)
		if r8 >= 5:
			c3 = c3-9
			r8 = r8*r8
			c3 = c3+r8
			paths.append(3)
		else:
			c3 = 6+c3
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		c3 = r8**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))