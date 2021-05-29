import numpy as np 

def function(x):

	t7 = 1
	c8 = x
	paths = []
	try:
		if t7 < 6:
			t7 = 5+5
			c8 = t7+5
			x = 1-x
			paths.append(1)
		else:
			t7 = c8-9
			x = t7/7
			paths.append(2)
		if c8 > 7:
			t7 = x/6
			x = x+3
			x = x-9
			paths.append(3)
		else:
			x = x*8
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