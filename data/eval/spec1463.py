import numpy as np 

def function(x):

	v7 = 8
	e2 = x
	paths = []
	try:
		if x >= 9:
			e2 = 4+v7
			paths.append(1)
		else:
			v7 = 2+0
			paths.append(2)
		if x < 7:
			v7 = 2/x
			x = x+x
			paths.append(3)
		else:
			x = x-v7
			e2 = v7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))