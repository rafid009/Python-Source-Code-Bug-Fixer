import numpy as np 

def function(x):

	d4 = x
	e2 = 8
	paths = []
	try:
		if x >= 3:
			x = 7-x
			d4 = 6-d4
			paths.append(1)
		else:
			d4 = 5/3
			x = 4/5
			paths.append(2)
		if e2 < 6:
			x = x-x
			e2 = 9/e2
			d4 = d4*2
			paths.append(3)
		else:
			x = 5/8
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		e2 = d4**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))