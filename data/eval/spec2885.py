import numpy as np 

def function(x):

	e5 = x
	w5 = x
	paths = []
	try:
		if w5 < 2:
			e5 = e5/5
			paths.append(1)
		else:
			x = x+3
			w5 = w5+2
			w5 = w5/w5
			paths.append(2)
		if w5 < 1:
			x = 3*9
			paths.append(3)
		else:
			x = w5/x
			x = w5-3
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		e5 = w5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))