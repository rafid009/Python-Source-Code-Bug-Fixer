import numpy as np 

def function(x):

	e4 = x
	d6 = 7
	paths = []
	try:
		if d6 >= 8:
			e4 = 9*7
			e4 = e4*5
			paths.append(1)
		else:
			e4 = x*7
			paths.append(2)
		if e4 < 1:
			e4 = 5+e4
			x = 1*5
			paths.append(3)
		else:
			d6 = 5*7
			d6 = e4/d6
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))