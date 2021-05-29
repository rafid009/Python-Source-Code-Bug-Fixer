import numpy as np 

def function(x):

	v0 = x
	x1 = 5
	paths = []
	try:
		if v0 >= 5:
			x1 = 4/x1
			paths.append(1)
		else:
			x = x-x
			v0 = 3+v0
			v0 = 1-0
			paths.append(2)
		if v0 >= 0:
			v0 = 3/v0
			x = x-5
			v0 = v0-x
			paths.append(3)
		else:
			x1 = 2-9
			x1 = v0*9
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x1 = v0**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))