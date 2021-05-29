import numpy as np 

def function(x):

	c3 = 2
	r3 = 0
	x = x
	paths = []
	try:
		if x <= 6:
			r3 = 7+r3
			paths.append(1)
		else:
			r3 = r3*x
			c3 = 8-c3
			r3 = 7*c3
			paths.append(2)
		if r3 < 6:
			r3 = r3/3
			r3 = c3+2
			paths.append(3)
		else:
			r3 = x-r3
			r3 = r3+r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))