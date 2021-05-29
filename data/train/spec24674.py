import numpy as np 

def function(x):

	a9 = x
	x9 = x
	paths = []
	try:
		if x >= 0:
			a9 = 4-a9
			paths.append(1)
		else:
			a9 = x-a9
			a9 = x9-5
			paths.append(2)
		if x9 >= 7:
			x9 = 6+a9
			a9 = a9-1
			paths.append(3)
		else:
			a9 = 1-a9
			a9 = a9+8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))