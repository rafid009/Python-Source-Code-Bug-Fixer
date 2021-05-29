import numpy as np 

def function(x):

	b4 = 1
	a0 = 8
	paths = []
	try:
		if b4 <= 7:
			b4 = 1-x
			a0 = 2/7
			paths.append(1)
		else:
			a0 = a0-5
			b4 = 2*x
			a0 = a0+4
			paths.append(2)
		if b4 < 3:
			a0 = b4*a0
			b4 = b4-a0
			paths.append(3)
		else:
			b4 = b4-8
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