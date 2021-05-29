import numpy as np 

def function(x):

	e7 = x
	a7 = 3
	x = x
	paths = []
	try:
		if e7 > 3:
			a7 = 2+a7
			x = 6-x
			x = 8-x
			paths.append(1)
		else:
			e7 = 7/e7
			x = x/6
			a7 = 1-6
			paths.append(2)
		if e7 < 3:
			e7 = a7+e7
			a7 = 5/8
			paths.append(3)
		else:
			a7 = a7-3
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