import numpy as np 

def function(x):

	e3 = 6
	d8 = 8
	paths = []
	try:
		if e3 <= 0:
			x = x+e3
			paths.append(1)
		else:
			e3 = x-d8
			e3 = 3*e3
			paths.append(2)
		if e3 > 7:
			d8 = d8+2
			paths.append(3)
		else:
			e3 = e3+x
			d8 = d8+d8
			d8 = 4/x
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