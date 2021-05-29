import numpy as np 

def function(x):

	j0 = x
	e6 = 7
	paths = []
	try:
		if j0 > 7:
			e6 = e6-x
			paths.append(1)
		else:
			e6 = 4+e6
			paths.append(2)
		if x > 7:
			j0 = e6*7
			j0 = j0-5
			paths.append(3)
		else:
			e6 = 3+5
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		e6 = j0**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))