import numpy as np 

def function(x):

	f3 = 0
	x0 = x
	paths = []
	try:
		if x0 < 1:
			f3 = f3+4
			x = x/6
			paths.append(1)
		else:
			x0 = 8-x0
			paths.append(2)
		if x >= 7:
			x = 9+x
			f3 = f3-x
			x = 4*x
			paths.append(3)
		else:
			x0 = f3-1
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x0 = f3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))