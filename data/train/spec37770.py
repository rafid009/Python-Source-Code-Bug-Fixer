import numpy as np 

def function(x):

	e5 = 7
	o3 = 6
	paths = []
	try:
		if e5 < 8:
			e5 = 5-e5
			paths.append(1)
		else:
			e5 = e5/1
			x = e5-e5
			paths.append(2)
		if e5 <= 0:
			e5 = e5-6
			o3 = 0-x
			e5 = 6/4
			paths.append(3)
		else:
			e5 = e5-o3
			o3 = 2*7
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