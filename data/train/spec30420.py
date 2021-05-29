import numpy as np 

def function(x):

	f9 = x
	e5 = 6
	paths = []
	try:
		if f9 >= 6:
			e5 = 0-e5
			f9 = 8-2
			paths.append(1)
		else:
			x = 2*f9
			x = f9/e5
			paths.append(2)
		if f9 >= 3:
			f9 = 4+0
			paths.append(3)
		else:
			f9 = 6/f9
			e5 = 7-e5
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))