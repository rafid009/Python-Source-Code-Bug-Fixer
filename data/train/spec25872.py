import numpy as np 

def function(x):

	f9 = 8
	w5 = x
	paths = []
	try:
		if w5 < 6:
			f9 = w5/w5
			f9 = 9/8
			w5 = w5*x
			paths.append(1)
		else:
			w5 = 9-w5
			x = f9-5
			paths.append(2)
		if x > 8:
			f9 = f9/1
			paths.append(3)
		else:
			f9 = 1*f9
			x = w5+2
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