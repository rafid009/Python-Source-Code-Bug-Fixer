import numpy as np 

def function(x):

	f4 = x
	x3 = 5
	paths = []
	try:
		if f4 >= 2:
			x3 = 9*x3
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if f4 > 6:
			f4 = 1*f4
			x3 = 3+x3
			f4 = 7-8
			paths.append(3)
		else:
			f4 = f4+f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))