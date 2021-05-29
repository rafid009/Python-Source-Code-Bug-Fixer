import numpy as np 

def function(x):

	e9 = 5
	s3 = 9
	paths = []
	try:
		if e9 < 9:
			e9 = s3+e9
			paths.append(1)
		else:
			e9 = e9+0
			paths.append(2)
		if x >= 6:
			x = x-7
			e9 = e9-0
			x = x-9
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))