import numpy as np 

def function(x):

	f4 = 5
	e5 = 8
	paths = []
	try:
		if x >= 9:
			f4 = 3-f4
			paths.append(1)
		else:
			f4 = 6*f4
			f4 = f4*9
			paths.append(2)
		if e5 >= 3:
			f4 = 1-x
			x = 8+3
			paths.append(3)
		else:
			e5 = e5/4
			x = x/4
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