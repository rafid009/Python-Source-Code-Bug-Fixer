import numpy as np 

def function(x):

	f8 = 8
	u0 = x
	x = x
	paths = []
	try:
		if u0 < 6:
			x = 3*u0
			f8 = 1-6
			x = f8-x
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if f8 < 8:
			f8 = 3+f8
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))