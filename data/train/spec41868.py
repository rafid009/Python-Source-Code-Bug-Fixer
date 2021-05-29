import numpy as np 

def function(x):

	w9 = x
	x4 = 5
	paths = []
	try:
		if x4 > 0:
			x4 = w9*6
			paths.append(1)
		else:
			x4 = 6*x4
			paths.append(2)
		if x < 8:
			x = x/2
			x4 = 1-w9
			paths.append(3)
		else:
			w9 = w9/2
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x4 = w9**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))