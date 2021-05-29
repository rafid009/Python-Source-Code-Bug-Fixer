import numpy as np 

def function(x):

	w0 = 6
	a7 = 9
	paths = []
	try:
		if x <= 4:
			a7 = a7+6
			paths.append(1)
		else:
			a7 = a7/3
			a7 = 9-a7
			paths.append(2)
		if w0 > 5:
			w0 = 6+5
			a7 = a7*a7
			paths.append(3)
		else:
			a7 = 9-3
			x = 8+5
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