import numpy as np 

def function(x):

	e7 = 6
	d6 = x
	paths = []
	try:
		if d6 <= 6:
			d6 = 9-4
			paths.append(1)
		else:
			x = 7+e7
			e7 = 9*3
			paths.append(2)
		if x >= 5:
			d6 = 8+d6
			e7 = 3*e7
			paths.append(3)
		else:
			d6 = d6+1
			d6 = 0*d6
			d6 = d6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))