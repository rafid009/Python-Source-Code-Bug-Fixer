import numpy as np 

def function(x):

	w5 = 0
	x3 = x
	paths = []
	try:
		if w5 >= 7:
			x = 5*x
			paths.append(1)
		else:
			w5 = x3*w5
			paths.append(2)
		if x <= 2:
			w5 = w5-4
			w5 = w5/8
			paths.append(3)
		else:
			x3 = 1*x3
			x3 = 0+w5
			x = x-3
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