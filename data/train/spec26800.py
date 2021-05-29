import numpy as np 

def function(x):

	a2 = x
	c3 = x
	paths = []
	try:
		if c3 > 1:
			x = 4+x
			a2 = a2*x
			x = x+8
			paths.append(1)
		else:
			x = a2*x
			paths.append(2)
		if a2 > 9:
			c3 = 1/8
			a2 = a2-1
			paths.append(3)
		else:
			c3 = c3/x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))