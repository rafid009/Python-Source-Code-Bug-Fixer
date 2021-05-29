import numpy as np 

def function(x):

	b2 = 1
	a0 = 3
	paths = []
	try:
		if a0 < 5:
			a0 = a0-7
			paths.append(1)
		else:
			b2 = b2-b2
			paths.append(2)
		if a0 > 0:
			b2 = 6/b2
			a0 = a0/9
			b2 = b2/9
			paths.append(3)
		else:
			a0 = a0*a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))