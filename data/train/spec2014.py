import numpy as np 

def function(x):

	w7 = 0
	f5 = x
	paths = []
	try:
		if x > 3:
			f5 = f5*9
			paths.append(1)
		else:
			w7 = 7+8
			w7 = 3-2
			paths.append(2)
		if x <= 6:
			f5 = f5+3
			w7 = 9+3
			paths.append(3)
		else:
			x = x/x
			f5 = 6*f5
			x = 8+w7
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