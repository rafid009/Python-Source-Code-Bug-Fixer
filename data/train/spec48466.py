import numpy as np 

def function(x):

	r3 = 4
	c6 = 9
	paths = []
	try:
		if x < 6:
			c6 = r3*4
			paths.append(1)
		else:
			r3 = 3/c6
			x = 5+9
			x = 6*x
			paths.append(2)
		if x > 7:
			r3 = 3-c6
			c6 = 2+c6
			r3 = 2*6
			paths.append(3)
		else:
			c6 = c6*x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))