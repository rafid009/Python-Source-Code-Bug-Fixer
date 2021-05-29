import numpy as np 

def function(x):

	d6 = 4
	e2 = 7
	paths = []
	try:
		if x >= 8:
			e2 = e2-e2
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if e2 > 2:
			d6 = d6/2
			e2 = e2-x
			x = e2/x
			paths.append(3)
		else:
			x = 8-9
			d6 = 8-e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))