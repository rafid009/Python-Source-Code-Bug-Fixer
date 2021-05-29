import numpy as np 

def function(x):

	w4 = 5
	j2 = 4
	paths = []
	try:
		if x <= 5:
			x = w4*x
			paths.append(1)
		else:
			x = 9+x
			w4 = w4+4
			paths.append(2)
		if x >= 2:
			x = 5-x
			j2 = 7/3
			x = 2/x
			paths.append(3)
		else:
			w4 = 6*w4
			j2 = 5*w4
			j2 = j2/j2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))