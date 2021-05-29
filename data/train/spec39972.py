import numpy as np 

def function(x):

	o6 = 0
	a3 = 1
	paths = []
	try:
		if a3 < 1:
			o6 = a3+1
			x = a3*x
			paths.append(1)
		else:
			o6 = o6+6
			paths.append(2)
		if o6 <= 9:
			o6 = 6/3
			x = 2-x
			paths.append(3)
		else:
			x = 4*x
			a3 = 3*8
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