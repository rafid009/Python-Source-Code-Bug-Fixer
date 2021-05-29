import numpy as np 

def function(x):

	e9 = 4
	d1 = 1
	paths = []
	try:
		if x <= 8:
			d1 = 3*1
			d1 = d1+3
			paths.append(1)
		else:
			d1 = 8+6
			d1 = 8*d1
			paths.append(2)
		if e9 <= 8:
			e9 = 4-e9
			paths.append(3)
		else:
			x = x+6
			d1 = d1/7
			e9 = d1/e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))