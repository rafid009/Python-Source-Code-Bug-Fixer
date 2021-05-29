import numpy as np 

def function(x):

	e0 = x
	d6 = x
	x = x
	paths = []
	try:
		if d6 > 4:
			x = d6*d6
			e0 = x-7
			paths.append(1)
		else:
			e0 = e0-2
			d6 = e0/8
			paths.append(2)
		if e0 <= 1:
			e0 = 5+8
			d6 = d6*d6
			d6 = d6/6
			paths.append(3)
		else:
			d6 = 8-d6
			x = 8+x
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