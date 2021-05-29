import numpy as np 

def function(x):

	y4 = 6
	e5 = 2
	paths = []
	try:
		if e5 < 3:
			y4 = y4*x
			paths.append(1)
		else:
			e5 = y4*6
			y4 = e5-5
			paths.append(2)
		if y4 > 9:
			x = x/y4
			y4 = 6/y4
			paths.append(3)
		else:
			e5 = e5-4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		e5 = y4**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))