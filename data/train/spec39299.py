import numpy as np 

def function(x):

	e7 = 3
	d0 = x
	paths = []
	try:
		if d0 > 9:
			e7 = 6+3
			paths.append(1)
		else:
			x = x/9
			x = x-6
			paths.append(2)
		if x >= 9:
			d0 = 1+d0
			paths.append(3)
		else:
			x = 5*1
			e7 = d0*e7
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		e7 = d0**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))