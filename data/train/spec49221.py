import numpy as np 

def function(x):

	e7 = 1
	a8 = x
	paths = []
	try:
		if e7 > 9:
			a8 = e7-e7
			e7 = x*x
			e7 = 8/a8
			paths.append(1)
		else:
			a8 = a8/8
			x = 4+x
			paths.append(2)
		if e7 > 8:
			e7 = 8+5
			a8 = a8+3
			x = x-e7
			paths.append(3)
		else:
			a8 = a8/8
			e7 = 4*1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))