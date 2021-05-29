import numpy as np 

def function(x):

	s7 = 4
	e9 = 7
	paths = []
	try:
		if s7 < 5:
			e9 = 2-x
			e9 = e9*2
			paths.append(1)
		else:
			x = 7/1
			paths.append(2)
		if x >= 5:
			e9 = e9/5
			e9 = e9/8
			x = e9-8
			paths.append(3)
		else:
			e9 = e9*2
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