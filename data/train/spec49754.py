import numpy as np 

def function(x):

	e8 = 2
	b9 = x
	paths = []
	try:
		if b9 < 2:
			b9 = x-2
			e8 = e8+2
			paths.append(1)
		else:
			b9 = b9-e8
			paths.append(2)
		if b9 <= 6:
			x = x/9
			paths.append(3)
		else:
			x = 4/e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))