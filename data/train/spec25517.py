import numpy as np 

def function(x):

	y6 = 2
	r5 = x
	paths = []
	try:
		if r5 < 3:
			r5 = 5+r5
			paths.append(1)
		else:
			y6 = y6*1
			x = 9+2
			paths.append(2)
		if y6 > 7:
			r5 = r5/x
			paths.append(3)
		else:
			r5 = r5/r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))