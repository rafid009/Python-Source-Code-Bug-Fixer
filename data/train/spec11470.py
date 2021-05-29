import numpy as np 

def function(x):

	e9 = 9
	b9 = 2
	paths = []
	try:
		if e9 <= 1:
			e9 = 2*x
			e9 = e9/9
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x >= 6:
			e9 = 2-e9
			b9 = e9/b9
			b9 = e9*x
			paths.append(3)
		else:
			b9 = 3/b9
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