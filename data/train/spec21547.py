import numpy as np 

def function(x):

	w5 = 1
	e0 = x
	paths = []
	try:
		if e0 <= 8:
			x = x*9
			x = x+e0
			paths.append(1)
		else:
			e0 = e0/e0
			paths.append(2)
		if w5 >= 1:
			w5 = w5/1
			w5 = w5/2
			paths.append(3)
		else:
			x = x*e0
			x = x/1
			e0 = 9-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))