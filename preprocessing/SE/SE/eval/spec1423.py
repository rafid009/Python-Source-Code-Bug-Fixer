import numpy as np 

def function(x):

	b9 = 3
	e6 = x
	x = x
	paths = []
	try:
		if x > 2:
			e6 = e6/4
			b9 = b9*5
			paths.append(1)
		else:
			b9 = b9*6
			paths.append(2)
		if e6 < 2:
			b9 = x+b9
			b9 = 1-b9
			paths.append(3)
		else:
			b9 = e6/b9
			x = x+b9
			b9 = 7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))