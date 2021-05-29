import numpy as np 

def function(x):

	e6 = 9
	b8 = 3
	paths = []
	try:
		if e6 >= 3:
			b8 = 7*b8
			paths.append(1)
		else:
			e6 = x-5
			b8 = b8*9
			x = x*e6
			paths.append(2)
		if b8 > 2:
			e6 = 7-4
			x = b8/x
			paths.append(3)
		else:
			b8 = b8+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))