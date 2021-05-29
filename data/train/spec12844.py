import numpy as np 

def function(x):

	y0 = x
	q4 = 7
	paths = []
	try:
		if q4 < 1:
			x = x-9
			paths.append(1)
		else:
			q4 = 9/q4
			paths.append(2)
		if x > 3:
			y0 = 3/1
			q4 = q4+x
			x = x/7
			paths.append(3)
		else:
			x = x*x
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