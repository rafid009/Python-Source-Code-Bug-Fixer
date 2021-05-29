import numpy as np 

def function(x):

	c9 = x
	r4 = x
	paths = []
	try:
		if r4 < 0:
			c9 = c9/8
			paths.append(1)
		else:
			x = x/x
			x = x*r4
			r4 = r4*4
			paths.append(2)
		if r4 >= 6:
			x = 9*x
			paths.append(3)
		else:
			c9 = x-4
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		r4 = c9**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))