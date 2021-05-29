import numpy as np 

def function(x):

	c3 = x
	u2 = 0
	paths = []
	try:
		if c3 < 4:
			u2 = u2-0
			c3 = c3*2
			x = u2/3
			paths.append(1)
		else:
			x = 2*x
			x = 1*7
			paths.append(2)
		if u2 >= 2:
			x = c3-c3
			paths.append(3)
		else:
			u2 = u2-5
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))