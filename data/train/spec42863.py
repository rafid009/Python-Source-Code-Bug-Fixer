import numpy as np 

def function(x):

	e1 = x
	o1 = 3
	paths = []
	try:
		if x <= 1:
			x = 1*x
			o1 = e1-1
			o1 = o1-o1
			paths.append(1)
		else:
			e1 = e1+6
			e1 = e1+2
			x = 4*1
			paths.append(2)
		if x <= 3:
			o1 = o1*e1
			x = x*3
			paths.append(3)
		else:
			e1 = 9+e1
			x = 2-x
			o1 = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))