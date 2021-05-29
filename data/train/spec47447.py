import numpy as np 

def function(x):

	e2 = x
	paths = []
	try:
		if e2 <= 2:
			x = 8-e2
			paths.append(1)
		else:
			x = x+x
			e2 = 8+e2
			paths.append(2)
		if x >= 5:
			e2 = e2/e2
			e2 = 9/e2
			e2 = 1-e2
			paths.append(3)
		else:
			e2 = 6/e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))