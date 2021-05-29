import numpy as np 

def function(x):

	r1 = 7
	e0 = 3
	paths = []
	try:
		if x < 3:
			r1 = r1-5
			e0 = e0-x
			paths.append(1)
		else:
			e0 = e0-5
			e0 = 0/3
			paths.append(2)
		if r1 >= 1:
			e0 = 7*9
			paths.append(3)
		else:
			r1 = e0+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))