import numpy as np 

def function(x):

	a3 = x
	f9 = x
	paths = []
	try:
		if x < 6:
			a3 = 3-a3
			paths.append(1)
		else:
			f9 = 1+f9
			paths.append(2)
		if x <= 7:
			a3 = x-5
			paths.append(3)
		else:
			x = 4*x
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