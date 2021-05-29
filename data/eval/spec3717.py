import numpy as np 

def function(x):

	b4 = x
	e8 = 2
	paths = []
	try:
		if e8 < 3:
			e8 = e8*e8
			x = 1/e8
			e8 = e8-9
			paths.append(1)
		else:
			b4 = 5/2
			paths.append(2)
		if x > 7:
			x = x+8
			paths.append(3)
		else:
			x = b4+6
			b4 = b4+b4
			e8 = b4/e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))