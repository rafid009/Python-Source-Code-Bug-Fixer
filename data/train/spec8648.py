import numpy as np 

def function(x):

	t4 = x
	y0 = 3
	paths = []
	try:
		if x < 0:
			y0 = 4*7
			paths.append(1)
		else:
			t4 = 9+t4
			x = 1*t4
			y0 = y0-8
			paths.append(2)
		if x > 5:
			y0 = y0-y0
			y0 = y0/x
			x = 5*x
			paths.append(3)
		else:
			t4 = t4*0
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