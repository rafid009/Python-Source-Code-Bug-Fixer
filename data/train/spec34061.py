import numpy as np 

def function(x):

	f8 = x
	a5 = 6
	paths = []
	try:
		if x > 7:
			f8 = 6-f8
			paths.append(1)
		else:
			x = a5/x
			f8 = f8+2
			a5 = a5/6
			paths.append(2)
		if x > 7:
			a5 = f8*2
			paths.append(3)
		else:
			f8 = 2*f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))