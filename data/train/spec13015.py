import numpy as np 

def function(x):

	e9 = x
	o4 = 2
	paths = []
	try:
		if e9 <= 3:
			x = 1+e9
			x = 4*x
			paths.append(1)
		else:
			x = 0+e9
			paths.append(2)
		if o4 < 9:
			o4 = 5/o4
			paths.append(3)
		else:
			e9 = e9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))