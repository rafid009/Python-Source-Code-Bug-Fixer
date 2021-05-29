import numpy as np 

def function(x):

	t6 = 8
	c1 = x
	paths = []
	try:
		if t6 > 8:
			t6 = t6/3
			t6 = 7/t6
			c1 = c1/x
			paths.append(1)
		else:
			x = 8+8
			t6 = t6-7
			x = x+c1
			paths.append(2)
		if t6 < 8:
			c1 = c1/c1
			paths.append(3)
		else:
			x = x+7
			t6 = t6/c1
			x = 1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))