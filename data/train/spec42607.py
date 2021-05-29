import numpy as np 

def function(x):

	e4 = x
	a8 = x
	paths = []
	try:
		if e4 >= 8:
			x = e4*3
			paths.append(1)
		else:
			x = x/6
			a8 = a8+3
			paths.append(2)
		if a8 >= 0:
			a8 = a8-0
			e4 = x/5
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		e4 = a8**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))