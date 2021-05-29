import numpy as np 

def function(x):

	e1 = x
	x9 = 8
	paths = []
	try:
		if x9 < 4:
			x9 = e1/x9
			paths.append(1)
		else:
			x9 = 2*e1
			x = x-6
			paths.append(2)
		if x9 > 1:
			x9 = x9*7
			paths.append(3)
		else:
			e1 = e1-x
			e1 = x/e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x9 = e1**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))