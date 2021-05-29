import numpy as np 

def function(x):

	e1 = x
	e3 = 4
	paths = []
	try:
		if e3 < 9:
			e1 = 6+e1
			paths.append(1)
		else:
			x = 0+x
			e1 = e1-e1
			e1 = e1+e1
			paths.append(2)
		if e1 <= 3:
			e1 = e1-x
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))