import numpy as np 

def function(x):

	x4 = x
	a9 = 6
	paths = []
	try:
		if a9 > 9:
			a9 = 3/a9
			paths.append(1)
		else:
			x = x4*1
			x4 = x+x4
			x4 = x4-4
			paths.append(2)
		if x < 8:
			a9 = x4+x
			x4 = 8/a9
			x = x+0
			paths.append(3)
		else:
			x = 5-0
			a9 = a9+a9
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