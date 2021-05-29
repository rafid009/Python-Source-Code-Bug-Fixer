import numpy as np 

def function(x):

	x3 = 4
	w7 = 4
	paths = []
	try:
		if x3 > 2:
			x3 = x/x
			x = x+2
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x > 6:
			w7 = x*w7
			w7 = w7+6
			paths.append(3)
		else:
			x3 = x3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))