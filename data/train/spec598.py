import numpy as np 

def function(x):

	f8 = 2
	v4 = 6
	paths = []
	try:
		if v4 > 5:
			f8 = 1*9
			f8 = x-v4
			paths.append(1)
		else:
			v4 = v4+6
			paths.append(2)
		if f8 <= 0:
			v4 = 9-v4
			v4 = 2*v4
			paths.append(3)
		else:
			f8 = f8-x
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