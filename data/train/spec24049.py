import numpy as np 

def function(x):

	e2 = x
	w4 = x
	x = x
	paths = []
	try:
		if x >= 1:
			x = 3/x
			paths.append(1)
		else:
			e2 = 7+w4
			paths.append(2)
		if e2 <= 2:
			w4 = x+e2
			paths.append(3)
		else:
			w4 = w4+6
			w4 = w4/3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))