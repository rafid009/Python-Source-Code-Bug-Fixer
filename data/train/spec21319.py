import numpy as np 

def function(x):

	e3 = 1
	e2 = 1
	paths = []
	try:
		if x <= 0:
			e2 = e2/1
			paths.append(1)
		else:
			e2 = 1-5
			e3 = 1*x
			e2 = 3/e2
			paths.append(2)
		if e2 > 6:
			e3 = 8*x
			paths.append(3)
		else:
			e2 = 7-e3
			e3 = 2-e3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e3 = e2**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))