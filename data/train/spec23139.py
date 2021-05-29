import numpy as np 

def function(x):

	x3 = 0
	a4 = 4
	paths = []
	try:
		if x3 <= 2:
			a4 = a4-a4
			x = x3*x3
			paths.append(1)
		else:
			x = x3-x3
			paths.append(2)
		if x < 9:
			x3 = 1-x3
			x = x-2
			x = x/3
			paths.append(3)
		else:
			x = x/4
			x = x*1
			x3 = a4+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))