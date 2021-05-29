import numpy as np 

def function(x):

	e5 = 8
	g3 = 1
	paths = []
	try:
		if e5 < 4:
			e5 = 3+x
			g3 = e5*g3
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if x <= 3:
			e5 = x-e5
			paths.append(3)
		else:
			e5 = e5+e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))