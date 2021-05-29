import numpy as np 

def function(x):

	c8 = x
	t4 = 3
	x = x
	paths = []
	try:
		if x < 3:
			c8 = 5+t4
			paths.append(1)
		else:
			c8 = c8+4
			t4 = t4-c8
			paths.append(2)
		if x <= 0:
			x = 4/x
			paths.append(3)
		else:
			c8 = x+6
			t4 = t4-8
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