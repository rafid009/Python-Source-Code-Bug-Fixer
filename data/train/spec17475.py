import numpy as np 

def function(x):

	e7 = x
	x9 = x
	x = x
	paths = []
	try:
		if e7 < 6:
			x = e7-x
			paths.append(1)
		else:
			x9 = 3/e7
			paths.append(2)
		if x9 < 4:
			x9 = x9-9
			x9 = e7+e7
			paths.append(3)
		else:
			e7 = 7+7
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