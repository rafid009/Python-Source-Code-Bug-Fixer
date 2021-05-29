import numpy as np 

def function(x):

	b5 = 2
	e3 = 4
	paths = []
	try:
		if e3 <= 6:
			b5 = b5-7
			e3 = e3-5
			paths.append(1)
		else:
			x = 8/e3
			e3 = e3/x
			paths.append(2)
		if b5 >= 2:
			x = x/x
			paths.append(3)
		else:
			x = x-5
			b5 = 8-b5
			e3 = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))