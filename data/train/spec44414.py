import numpy as np 

def function(x):

	x8 = x
	e7 = 5
	paths = []
	try:
		if e7 <= 8:
			e7 = 2-e7
			paths.append(1)
		else:
			x = 2*x
			x8 = 5+x8
			x = x8-0
			paths.append(2)
		if e7 <= 6:
			x8 = x/2
			x8 = 6-x8
			paths.append(3)
		else:
			x8 = 4/e7
			e7 = 1/e7
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))