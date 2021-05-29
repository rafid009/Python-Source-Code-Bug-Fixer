import numpy as np 

def function(x):

	y7 = x
	t6 = 1
	x = 0
	paths = []
	try:
		if x < 3:
			x = x*t6
			t6 = 0-t6
			paths.append(1)
		else:
			t6 = t6*6
			y7 = 2*x
			paths.append(2)
		if x > 8:
			t6 = t6-x
			paths.append(3)
		else:
			t6 = 7+0
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))