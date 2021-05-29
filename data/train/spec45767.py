import numpy as np 

def function(x):

	c2 = x
	u0 = x
	paths = []
	try:
		if x < 8:
			c2 = c2+1
			paths.append(1)
		else:
			u0 = u0/4
			u0 = u0-u0
			paths.append(2)
		if u0 <= 6:
			c2 = c2-c2
			c2 = c2-3
			paths.append(3)
		else:
			c2 = c2*c2
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))