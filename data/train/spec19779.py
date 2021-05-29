import numpy as np 

def function(x):

	y0 = 6
	e5 = 3
	paths = []
	try:
		if x <= 5:
			e5 = e5/2
			y0 = y0*2
			e5 = e5+x
			paths.append(1)
		else:
			x = y0/y0
			y0 = x/y0
			e5 = 6+8
			paths.append(2)
		if x >= 8:
			x = 5+x
			x = e5*x
			paths.append(3)
		else:
			e5 = 4-e5
			y0 = 0/1
			y0 = 7/5
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