import numpy as np 

def function(x):

	a2 = x
	x5 = 2
	paths = []
	try:
		if a2 >= 9:
			a2 = 9+a2
			a2 = a2*4
			a2 = 4*a2
			paths.append(1)
		else:
			x5 = x5-3
			paths.append(2)
		if x5 >= 6:
			a2 = x5/a2
			x5 = x*1
			paths.append(3)
		else:
			a2 = 4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))