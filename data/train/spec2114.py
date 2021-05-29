import numpy as np 

def function(x):

	w6 = 6
	e8 = 3
	paths = []
	try:
		if e8 <= 4:
			w6 = 3/w6
			w6 = w6*9
			paths.append(1)
		else:
			x = 8-3
			e8 = e8*e8
			paths.append(2)
		if w6 >= 8:
			w6 = w6/x
			w6 = w6*9
			paths.append(3)
		else:
			x = 2+x
			w6 = 3-e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))