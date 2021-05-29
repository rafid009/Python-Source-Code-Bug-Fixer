import numpy as np 

def function(x):

	b4 = x
	e0 = 2
	x = 4
	paths = []
	try:
		if e0 <= 2:
			e0 = x-e0
			x = x-8
			x = x/2
			paths.append(1)
		else:
			x = 7+b4
			b4 = b4*8
			x = x/b4
			paths.append(2)
		if e0 > 9:
			b4 = x*b4
			x = x-0
			paths.append(3)
		else:
			e0 = b4+e0
			b4 = 6*b4
			e0 = e0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))