import numpy as np 

def function(x):

	f4 = 0
	a8 = 9
	paths = []
	try:
		if f4 >= 0:
			f4 = 0-f4
			f4 = f4-x
			paths.append(1)
		else:
			a8 = 4/6
			x = 7-x
			a8 = a8*a8
			paths.append(2)
		if a8 <= 2:
			x = 3+3
			x = f4+x
			f4 = a8/8
			paths.append(3)
		else:
			x = 8/x
			a8 = x-a8
			f4 = f4-f4
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