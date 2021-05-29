import numpy as np 

def function(x):

	f0 = 4
	a5 = 4
	paths = []
	try:
		if a5 < 0:
			x = f0-3
			f0 = a5-x
			f0 = f0/f0
			paths.append(1)
		else:
			a5 = a5-8
			a5 = 2/a5
			paths.append(2)
		if f0 < 5:
			a5 = a5*f0
			x = 3-f0
			a5 = 1-4
			paths.append(3)
		else:
			a5 = 3*6
			a5 = 7/x
			a5 = a5-2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))