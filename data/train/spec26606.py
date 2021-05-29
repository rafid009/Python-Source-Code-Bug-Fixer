import numpy as np 

def function(x):

	e4 = x
	d4 = 6
	paths = []
	try:
		if x > 4:
			e4 = 3/e4
			paths.append(1)
		else:
			e4 = e4-0
			d4 = 0*9
			e4 = e4/6
			paths.append(2)
		if d4 > 3:
			x = e4/x
			e4 = d4/8
			paths.append(3)
		else:
			e4 = e4+6
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