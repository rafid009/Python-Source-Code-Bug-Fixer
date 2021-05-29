import numpy as np 

def function(x):

	e7 = x
	e2 = x
	x = 8
	paths = []
	try:
		if e2 >= 8:
			e7 = e7*1
			paths.append(1)
		else:
			e7 = e7/3
			e2 = 8+e2
			x = e7*4
			paths.append(2)
		if e7 <= 0:
			e2 = e2*4
			e7 = e7/e7
			x = e7-x
			paths.append(3)
		else:
			e7 = 2*6
			e2 = e2*e7
			x = 5*x
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