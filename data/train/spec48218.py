import numpy as np 

def function(x):

	x6 = x
	w9 = x
	paths = []
	try:
		if x < 4:
			x = x+3
			x = 0-x
			paths.append(1)
		else:
			x = w9/w9
			w9 = 8*w9
			x = x*5
			paths.append(2)
		if x < 8:
			x = x*x6
			paths.append(3)
		else:
			x = 5+4
			w9 = 9*w9
			w9 = 6*w9
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