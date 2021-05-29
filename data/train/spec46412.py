import numpy as np 

def function(x):

	n8 = 0
	e9 = x
	paths = []
	try:
		if e9 < 4:
			x = 2+x
			paths.append(1)
		else:
			x = x+7
			e9 = e9/x
			paths.append(2)
		if x <= 0:
			e9 = 5-e9
			paths.append(3)
		else:
			e9 = e9*x
			x = e9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))