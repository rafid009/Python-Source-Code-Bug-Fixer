import numpy as np 

def function(x):

	e5 = 1
	i0 = 8
	paths = []
	try:
		if e5 <= 0:
			i0 = 2*4
			i0 = i0*i0
			x = 3*e5
			paths.append(1)
		else:
			i0 = i0+2
			paths.append(2)
		if e5 <= 1:
			e5 = e5*e5
			paths.append(3)
		else:
			x = 6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))