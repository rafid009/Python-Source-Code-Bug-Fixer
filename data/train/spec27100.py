import numpy as np 

def function(x):

	w3 = 8
	r3 = 8
	x = 0
	paths = []
	try:
		if r3 <= 2:
			w3 = w3*x
			paths.append(1)
		else:
			r3 = r3+w3
			w3 = w3*7
			x = x-5
			paths.append(2)
		if r3 <= 5:
			x = 3*x
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))