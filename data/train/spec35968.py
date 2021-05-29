import numpy as np 

def function(x):

	v0 = x
	c3 = x
	x = 1
	paths = []
	try:
		if x >= 7:
			x = x-c3
			paths.append(1)
		else:
			c3 = c3/5
			paths.append(2)
		if x >= 2:
			c3 = 4*c3
			v0 = 5+5
			v0 = 2*v0
			paths.append(3)
		else:
			c3 = c3/x
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))