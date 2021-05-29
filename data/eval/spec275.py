import numpy as np 

def function(x):

	e4 = 4
	w7 = x
	paths = []
	try:
		if w7 > 4:
			e4 = 4*e4
			w7 = w7*x
			paths.append(1)
		else:
			e4 = e4*0
			e4 = e4+8
			paths.append(2)
		if w7 > 4:
			x = x-4
			w7 = w7-5
			e4 = e4*0
			paths.append(3)
		else:
			e4 = 6-0
			w7 = 3+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))