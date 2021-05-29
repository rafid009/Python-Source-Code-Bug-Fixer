import numpy as np 

def function(x):

	c2 = x
	t0 = x
	paths = []
	try:
		if c2 <= 4:
			t0 = 9*t0
			paths.append(1)
		else:
			c2 = x+6
			t0 = 3-7
			x = x+x
			paths.append(2)
		if t0 <= 8:
			x = x*7
			x = 1-x
			paths.append(3)
		else:
			x = x*1
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))