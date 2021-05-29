import numpy as np 

def function(x):

	c3 = 8
	a4 = x
	paths = []
	try:
		if c3 > 9:
			x = x/a4
			x = a4/a4
			a4 = 9+2
			paths.append(1)
		else:
			x = x+5
			c3 = c3/x
			x = x+x
			paths.append(2)
		if x > 1:
			c3 = 7+x
			c3 = c3+x
			c3 = 1-x
			paths.append(3)
		else:
			c3 = c3/x
			x = c3*a4
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