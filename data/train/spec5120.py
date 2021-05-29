import numpy as np 

def function(x):

	x8 = x
	e2 = x
	paths = []
	try:
		if x8 < 0:
			x8 = x8/x
			paths.append(1)
		else:
			e2 = 9/e2
			e2 = e2/5
			x = x+1
			paths.append(2)
		if x8 <= 3:
			e2 = 6/4
			x8 = 3-x8
			paths.append(3)
		else:
			e2 = 8/e2
			x8 = 2-x
			x = 0*x
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