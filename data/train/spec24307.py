import numpy as np 

def function(x):

	n4 = 1
	e3 = x
	paths = []
	try:
		if n4 >= 0:
			e3 = e3*5
			n4 = 0-7
			paths.append(1)
		else:
			n4 = 0-0
			paths.append(2)
		if x > 9:
			x = 4*5
			paths.append(3)
		else:
			n4 = n4*2
			e3 = e3/8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		e3 = n4**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))