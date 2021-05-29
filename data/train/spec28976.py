import numpy as np 

def function(x):

	t0 = x
	y7 = 4
	x = 3
	paths = []
	try:
		if x <= 9:
			t0 = 6*t0
			x = x-t0
			x = 8*x
			paths.append(1)
		else:
			t0 = 4+2
			t0 = t0/3
			paths.append(2)
		if y7 >= 3:
			x = 2/x
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))