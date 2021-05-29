import numpy as np 

def function(x):

	q3 = x
	r2 = 5
	paths = []
	try:
		if x < 7:
			x = x*4
			paths.append(1)
		else:
			x = x*6
			q3 = 0-q3
			paths.append(2)
		if r2 < 5:
			x = 7-5
			paths.append(3)
		else:
			r2 = 5/q3
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