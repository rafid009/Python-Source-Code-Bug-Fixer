import numpy as np 

def function(x):

	e6 = x
	e1 = x
	paths = []
	try:
		if e1 < 6:
			e6 = 0-e6
			paths.append(1)
		else:
			e1 = e1+e1
			e6 = 8-7
			x = x+4
			paths.append(2)
		if x <= 8:
			e1 = 0*3
			e1 = x+e1
			e6 = 7-e6
			paths.append(3)
		else:
			e6 = 1/e1
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e1 = e6**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))