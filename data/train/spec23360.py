import numpy as np 

def function(x):

	b2 = 0
	e5 = x
	paths = []
	try:
		if e5 <= 1:
			b2 = 6*7
			paths.append(1)
		else:
			b2 = 0-2
			paths.append(2)
		if b2 > 1:
			x = 1*x
			e5 = 5*4
			paths.append(3)
		else:
			e5 = x+4
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))