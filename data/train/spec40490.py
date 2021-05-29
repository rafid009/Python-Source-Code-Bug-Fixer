import numpy as np 

def function(x):

	e0 = x
	e5 = 2
	paths = []
	try:
		if e5 >= 3:
			x = e0*1
			e0 = 1*e0
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if e5 < 5:
			e0 = x-e0
			e0 = 9-5
			e5 = x-e5
			paths.append(3)
		else:
			e0 = 0/e0
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e0 = e5**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))