import numpy as np 

def function(x):

	e1 = 7
	e3 = x
	paths = []
	try:
		if e3 >= 5:
			e1 = 4+e1
			x = 0+x
			paths.append(1)
		else:
			e1 = e1+8
			paths.append(2)
		if e1 > 3:
			e1 = 2/2
			e1 = e3+3
			x = e1+5
			paths.append(3)
		else:
			e3 = e3-e3
			e1 = 8/x
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