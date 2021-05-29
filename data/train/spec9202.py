import numpy as np 

def function(x):

	e0 = 5
	y5 = x
	x = x
	paths = []
	try:
		if y5 < 7:
			x = x+8
			e0 = e0-2
			y5 = y5/x
			paths.append(1)
		else:
			y5 = 1*5
			y5 = 2*y5
			x = x+e0
			paths.append(2)
		if e0 > 9:
			y5 = y5+2
			e0 = x-7
			paths.append(3)
		else:
			e0 = e0+e0
			x = x-e0
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		e0 = y5**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))