import numpy as np 

def function(x):

	t4 = 3
	c5 = x
	paths = []
	try:
		if c5 > 8:
			x = x+t4
			paths.append(1)
		else:
			c5 = 1*t4
			c5 = c5/4
			t4 = x+7
			paths.append(2)
		if t4 > 2:
			x = 9+x
			x = 3-x
			paths.append(3)
		else:
			c5 = 8+c5
			x = 8/x
			c5 = 3+t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))