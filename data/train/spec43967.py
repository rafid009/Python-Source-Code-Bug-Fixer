import numpy as np 

def function(x):

	e7 = x
	x9 = x
	paths = []
	try:
		if e7 > 9:
			x = 9+x
			paths.append(1)
		else:
			e7 = e7+e7
			x9 = x9-x9
			x9 = e7*x9
			paths.append(2)
		if e7 >= 9:
			x = x+x
			e7 = x9/e7
			x9 = 9-6
			paths.append(3)
		else:
			x9 = x9*0
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