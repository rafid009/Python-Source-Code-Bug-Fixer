import numpy as np 

def function(x):

	a9 = 4
	f1 = x
	paths = []
	try:
		if x <= 3:
			a9 = a9/2
			f1 = f1/8
			x = f1-0
			paths.append(1)
		else:
			f1 = f1*f1
			x = a9/x
			a9 = a9-6
			paths.append(2)
		if f1 < 6:
			a9 = x/x
			a9 = 1*a9
			f1 = 9+f1
			paths.append(3)
		else:
			x = x-6
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