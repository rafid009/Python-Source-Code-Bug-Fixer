import numpy as np 

def function(x):

	f7 = 8
	q6 = x
	paths = []
	try:
		if q6 > 9:
			x = f7/f7
			x = x*7
			x = x+f7
			paths.append(1)
		else:
			f7 = f7+x
			f7 = 9*f7
			q6 = q6*6
			paths.append(2)
		if q6 < 2:
			f7 = f7/5
			paths.append(3)
		else:
			x = x-3
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