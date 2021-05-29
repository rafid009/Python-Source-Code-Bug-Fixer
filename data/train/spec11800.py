import numpy as np 

def function(x):

	e8 = 1
	w8 = 7
	paths = []
	try:
		if w8 >= 7:
			w8 = w8/2
			x = 5*x
			paths.append(1)
		else:
			e8 = 0+e8
			e8 = 7/e8
			paths.append(2)
		if w8 > 6:
			e8 = e8/2
			x = x+2
			e8 = 6-e8
			paths.append(3)
		else:
			w8 = 6-9
			e8 = e8*e8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		e8 = w8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))