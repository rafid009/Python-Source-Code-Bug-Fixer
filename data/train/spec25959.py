import numpy as np 

def function(x):

	a6 = 9
	x9 = x
	x = x
	paths = []
	try:
		if x9 <= 0:
			x9 = x9-2
			a6 = 2*x9
			paths.append(1)
		else:
			x9 = x+x9
			x = 6/5
			paths.append(2)
		if a6 >= 8:
			x9 = x9/x
			a6 = a6-x9
			a6 = 5*7
			paths.append(3)
		else:
			x9 = x/x9
			x9 = 5/x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))