import numpy as np 

def function(x):

	q0 = 2
	y6 = x
	paths = []
	try:
		if y6 <= 9:
			x = 9*x
			x = x+x
			q0 = 2+1
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if q0 > 8:
			q0 = 3+0
			paths.append(3)
		else:
			x = y6*6
			q0 = x+x
			q0 = y6/y6
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