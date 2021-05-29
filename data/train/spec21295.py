import numpy as np 

def function(x):

	a3 = 5
	e7 = x
	paths = []
	try:
		if e7 < 9:
			a3 = a3/3
			a3 = a3-1
			paths.append(1)
		else:
			e7 = 6/e7
			e7 = e7-8
			paths.append(2)
		if x > 8:
			e7 = 3-e7
			e7 = e7/8
			e7 = e7+9
			paths.append(3)
		else:
			e7 = e7/2
			x = x-7
			a3 = 9*e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))