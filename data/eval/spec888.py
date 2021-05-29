import numpy as np 

def function(x):

	c3 = 8
	t9 = x
	paths = []
	try:
		if c3 < 6:
			c3 = t9*c3
			t9 = x+x
			c3 = x*9
			paths.append(1)
		else:
			t9 = t9+8
			x = x/x
			t9 = 7+t9
			paths.append(2)
		if x > 2:
			x = x+6
			t9 = 3/t9
			x = x/t9
			paths.append(3)
		else:
			x = 2*x
			t9 = t9-x
			x = 2*t9
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