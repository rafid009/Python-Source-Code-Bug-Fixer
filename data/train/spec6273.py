import numpy as np 

def function(x):

	y5 = x
	t9 = 1
	x = x
	paths = []
	try:
		if y5 >= 6:
			t9 = t9/5
			t9 = t9/5
			paths.append(1)
		else:
			y5 = 7/y5
			t9 = t9+6
			paths.append(2)
		if t9 < 0:
			y5 = 2/8
			t9 = t9/8
			paths.append(3)
		else:
			y5 = y5*y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))