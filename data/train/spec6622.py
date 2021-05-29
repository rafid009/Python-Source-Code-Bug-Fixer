import numpy as np 

def function(x):

	t0 = 7
	c9 = 1
	paths = []
	try:
		if c9 < 2:
			c9 = c9-9
			t0 = 9-1
			x = 7+x
			paths.append(1)
		else:
			c9 = c9/9
			paths.append(2)
		if c9 <= 8:
			c9 = c9-6
			c9 = 2*c9
			paths.append(3)
		else:
			c9 = c9+3
			c9 = 4+4
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))