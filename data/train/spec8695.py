import numpy as np 

def function(x):

	k9 = 1
	e8 = x
	paths = []
	try:
		if x >= 1:
			e8 = 5/e8
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x <= 1:
			e8 = e8*x
			x = 9-x
			paths.append(3)
		else:
			e8 = e8-3
			x = 8-0
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))