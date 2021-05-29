import numpy as np 

def function(x):

	x2 = 7
	e2 = 2
	paths = []
	try:
		if x2 > 6:
			e2 = e2*4
			x = 2+x
			e2 = x/4
			paths.append(1)
		else:
			x2 = x2+4
			x = x+x
			paths.append(2)
		if e2 > 7:
			x = 9/e2
			e2 = e2-2
			x2 = x2/x2
			paths.append(3)
		else:
			e2 = x+0
			x = x-x2
			x2 = 8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))