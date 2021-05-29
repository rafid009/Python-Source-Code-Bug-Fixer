import numpy as np 

def function(x):

	x7 = x
	a8 = 0
	paths = []
	try:
		if x7 >= 0:
			a8 = x*7
			x7 = 1-1
			a8 = a8*x
			paths.append(1)
		else:
			x = a8*x7
			x = x-4
			x7 = 6*x7
			paths.append(2)
		if x > 7:
			x7 = 7-4
			paths.append(3)
		else:
			a8 = 8+x7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))