import numpy as np 

def function(x):

	w9 = x
	i8 = 7
	paths = []
	try:
		if w9 < 5:
			i8 = w9/i8
			paths.append(1)
		else:
			w9 = w9*x
			x = x*i8
			paths.append(2)
		if i8 < 9:
			i8 = i8+6
			w9 = w9*i8
			paths.append(3)
		else:
			x = x*4
			i8 = i8/3
			i8 = i8-7
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