import numpy as np 

def function(x):

	w4 = x
	j2 = 3
	paths = []
	try:
		if w4 > 9:
			x = 9*x
			paths.append(1)
		else:
			j2 = x*3
			paths.append(2)
		if x >= 8:
			j2 = j2/w4
			paths.append(3)
		else:
			x = w4+w4
			x = 1/j2
			w4 = j2-8
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