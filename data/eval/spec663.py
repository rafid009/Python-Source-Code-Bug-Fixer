import numpy as np 

def function(x):

	w3 = 7
	e3 = 7
	paths = []
	try:
		if e3 >= 1:
			w3 = 3+w3
			x = x*e3
			paths.append(1)
		else:
			w3 = 9-1
			e3 = 8+e3
			paths.append(2)
		if x >= 1:
			e3 = 3-6
			e3 = 8-e3
			w3 = 4+w3
			paths.append(3)
		else:
			w3 = 5-w3
			e3 = 5+e3
			w3 = w3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))