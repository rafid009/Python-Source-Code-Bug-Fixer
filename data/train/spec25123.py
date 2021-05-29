import numpy as np 

def function(x):

	c9 = 6
	t1 = x
	paths = []
	try:
		if t1 >= 6:
			c9 = 4-5
			x = 0-5
			paths.append(1)
		else:
			t1 = t1-6
			paths.append(2)
		if t1 > 5:
			t1 = t1+t1
			paths.append(3)
		else:
			c9 = c9/t1
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