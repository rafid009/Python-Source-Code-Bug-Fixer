import numpy as np 

def function(x):

	e4 = 5
	e1 = x
	paths = []
	try:
		if x >= 0:
			e1 = e1-6
			paths.append(1)
		else:
			e4 = 3+e4
			e4 = 9+e4
			e4 = e4-9
			paths.append(2)
		if e1 > 6:
			e4 = 2-e4
			x = x-e1
			e1 = e1/4
			paths.append(3)
		else:
			e4 = e4+e4
			e4 = 3*1
			e4 = e4/8
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))