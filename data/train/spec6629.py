import numpy as np 

def function(x):

	c9 = 5
	r0 = x
	paths = []
	try:
		if x >= 6:
			c9 = c9+4
			x = x*c9
			x = x-6
			paths.append(1)
		else:
			c9 = c9*4
			paths.append(2)
		if x > 7:
			x = x+c9
			x = x+2
			paths.append(3)
		else:
			c9 = 0*c9
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))