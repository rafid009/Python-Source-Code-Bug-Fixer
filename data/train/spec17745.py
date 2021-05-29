import numpy as np 

def function(x):

	w1 = 5
	e0 = x
	paths = []
	try:
		if e0 >= 9:
			x = 7/x
			w1 = w1*e0
			x = 5/5
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if e0 > 2:
			x = 4+8
			e0 = x/w1
			paths.append(3)
		else:
			e0 = e0*e0
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