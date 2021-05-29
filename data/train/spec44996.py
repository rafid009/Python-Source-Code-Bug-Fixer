import numpy as np 

def function(x):

	e2 = 1
	x7 = 7
	paths = []
	try:
		if e2 < 1:
			x = x-1
			x7 = 9/x7
			x = x+9
			paths.append(1)
		else:
			x = x-e2
			x = e2/x
			e2 = e2/2
			paths.append(2)
		if e2 < 1:
			x = x+8
			e2 = e2-3
			paths.append(3)
		else:
			x = 3+5
			x7 = x7-4
			x7 = x-5
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))