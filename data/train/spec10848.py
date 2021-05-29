import numpy as np 

def function(x):

	f4 = 6
	a3 = x
	paths = []
	try:
		if x >= 0:
			a3 = f4*5
			x = f4+0
			a3 = 2/x
			paths.append(1)
		else:
			f4 = a3*f4
			paths.append(2)
		if x >= 4:
			a3 = a3/x
			paths.append(3)
		else:
			a3 = 7+f4
			f4 = f4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))