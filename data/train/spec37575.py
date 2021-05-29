import numpy as np 

def function(x):

	a7 = x
	e7 = 1
	x = x
	paths = []
	try:
		if a7 < 6:
			e7 = 7/e7
			a7 = 0+0
			a7 = a7+5
			paths.append(1)
		else:
			a7 = a7*a7
			a7 = a7+e7
			paths.append(2)
		if x > 2:
			x = x+a7
			a7 = a7+0
			paths.append(3)
		else:
			x = 0*x
			e7 = x-e7
			x = a7-6
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		a7 = e7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))