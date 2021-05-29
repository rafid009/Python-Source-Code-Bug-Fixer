import numpy as np 

def function(x):

	t0 = x
	y5 = 1
	paths = []
	try:
		if x >= 0:
			x = x*6
			t0 = y5+t0
			y5 = 3/9
			paths.append(1)
		else:
			x = 0-5
			paths.append(2)
		if y5 > 7:
			x = t0+x
			t0 = 7-y5
			t0 = t0/y5
			paths.append(3)
		else:
			y5 = y5-y5
			t0 = 5*t0
			t0 = t0+y5
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