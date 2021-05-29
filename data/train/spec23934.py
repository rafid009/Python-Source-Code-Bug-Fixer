import numpy as np 

def function(x):

	a9 = x
	a1 = 7
	paths = []
	try:
		if a1 < 9:
			a1 = a1/6
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x >= 7:
			x = 3+x
			paths.append(3)
		else:
			x = 2*x
			a1 = 4+a1
			a9 = a9/a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))