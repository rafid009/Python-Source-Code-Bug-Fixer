import numpy as np 

def function(x):

	f7 = 4
	v4 = x
	x = 5
	paths = []
	try:
		if x > 3:
			x = f7-9
			v4 = 4/v4
			paths.append(1)
		else:
			x = x-x
			v4 = v4/1
			v4 = 1-1
			paths.append(2)
		if v4 < 1:
			f7 = f7*9
			f7 = f7+v4
			paths.append(3)
		else:
			v4 = v4/v4
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