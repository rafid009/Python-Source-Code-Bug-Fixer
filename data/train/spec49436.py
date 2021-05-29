import numpy as np 

def function(x):

	y0 = x
	f6 = 8
	paths = []
	try:
		if f6 <= 6:
			x = 3+4
			f6 = f6*7
			paths.append(1)
		else:
			y0 = 5+y0
			x = x*4
			y0 = x-2
			paths.append(2)
		if x < 3:
			x = 7-x
			paths.append(3)
		else:
			x = y0*6
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))