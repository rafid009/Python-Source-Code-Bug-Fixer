import numpy as np 

def function(x):

	e8 = x
	q4 = x
	paths = []
	try:
		if q4 < 9:
			x = x+1
			paths.append(1)
		else:
			e8 = e8*3
			paths.append(2)
		if x > 1:
			e8 = 7+1
			e8 = e8-0
			e8 = 0/q4
			paths.append(3)
		else:
			x = 7*x
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))