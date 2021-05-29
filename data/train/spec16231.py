import numpy as np 

def function(x):

	a7 = x
	e2 = x
	paths = []
	try:
		if x < 2:
			e2 = e2*7
			paths.append(1)
		else:
			x = 0/x
			e2 = 9+e2
			x = 6/8
			paths.append(2)
		if a7 >= 8:
			a7 = 0-0
			e2 = e2-2
			a7 = 6-a7
			paths.append(3)
		else:
			e2 = 5-6
			e2 = 9/x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		a7 = e2**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))