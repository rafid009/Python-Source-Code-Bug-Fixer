import numpy as np 

def function(x):

	t1 = 7
	y0 = 2
	paths = []
	try:
		if x < 0:
			t1 = 1/x
			y0 = y0/3
			y0 = 5+y0
			paths.append(1)
		else:
			y0 = y0-6
			y0 = y0*9
			paths.append(2)
		if x < 7:
			t1 = 7/y0
			t1 = 7+x
			x = 9/8
			paths.append(3)
		else:
			x = 3/1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))