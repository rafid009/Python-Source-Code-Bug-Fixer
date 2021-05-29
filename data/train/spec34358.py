import numpy as np 

def function(x):

	f3 = 1
	v7 = x
	paths = []
	try:
		if f3 >= 8:
			v7 = 0+f3
			paths.append(1)
		else:
			f3 = 0-7
			x = 5/v7
			paths.append(2)
		if f3 > 7:
			x = x-x
			x = 1-0
			v7 = 9*v7
			paths.append(3)
		else:
			f3 = f3+6
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