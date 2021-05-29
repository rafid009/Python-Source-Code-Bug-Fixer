import numpy as np 

def function(x):

	e9 = x
	b4 = 6
	paths = []
	try:
		if b4 >= 2:
			b4 = b4*b4
			b4 = 2+2
			paths.append(1)
		else:
			b4 = e9*b4
			paths.append(2)
		if x <= 6:
			x = 3*4
			paths.append(3)
		else:
			e9 = 4*3
			x = 2-b4
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