import numpy as np 

def function(x):

	w9 = x
	x3 = x
	paths = []
	try:
		if x <= 9:
			w9 = w9-3
			w9 = x3+4
			x = w9*x
			paths.append(1)
		else:
			x = w9-w9
			x = x*w9
			paths.append(2)
		if x < 6:
			x3 = x3/6
			paths.append(3)
		else:
			x = x-x3
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))