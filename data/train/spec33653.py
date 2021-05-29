import numpy as np 

def function(x):

	c6 = x
	r5 = 9
	paths = []
	try:
		if c6 > 9:
			x = 3*r5
			paths.append(1)
		else:
			r5 = 6+r5
			paths.append(2)
		if r5 > 8:
			r5 = r5-r5
			paths.append(3)
		else:
			x = r5-1
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))