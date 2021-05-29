import numpy as np 

def function(x):

	a7 = x
	w5 = 4
	paths = []
	try:
		if x > 9:
			w5 = w5/8
			a7 = 7/7
			paths.append(1)
		else:
			w5 = w5*a7
			paths.append(2)
		if x > 6:
			a7 = a7+w5
			paths.append(3)
		else:
			a7 = a7/3
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))