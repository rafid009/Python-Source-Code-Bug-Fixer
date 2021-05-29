import numpy as np 

def function(x):

	x1 = 6
	f4 = 2
	paths = []
	try:
		if x1 < 3:
			x = f4+x
			f4 = f4/f4
			paths.append(1)
		else:
			f4 = 3+f4
			paths.append(2)
		if f4 < 0:
			f4 = 3+5
			x1 = f4-2
			x = 1+x
			paths.append(3)
		else:
			f4 = f4-7
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