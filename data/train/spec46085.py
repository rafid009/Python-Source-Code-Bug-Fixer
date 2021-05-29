import numpy as np 

def function(x):

	e9 = x
	a5 = x
	paths = []
	try:
		if a5 > 1:
			x = a5*5
			x = a5/x
			a5 = 4+a5
			paths.append(1)
		else:
			e9 = e9-0
			e9 = e9/a5
			x = x-e9
			paths.append(2)
		if x <= 7:
			e9 = e9/7
			x = a5+3
			paths.append(3)
		else:
			x = 1*1
			e9 = 8/4
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