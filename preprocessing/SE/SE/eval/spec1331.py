import numpy as np 

def function(x):

	y7 = x
	t0 = x
	paths = []
	try:
		if y7 <= 6:
			t0 = x*t0
			t0 = 8+5
			paths.append(1)
		else:
			t0 = y7/x
			x = t0*y7
			paths.append(2)
		if y7 >= 1:
			t0 = 1*t0
			x = 1/6
			x = 0*x
			paths.append(3)
		else:
			x = y7/t0
			y7 = y7-9
			t0 = t0/2
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