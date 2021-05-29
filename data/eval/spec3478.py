import numpy as np 

def function(x):

	j3 = x
	e9 = 8
	x = x
	paths = []
	try:
		if j3 < 7:
			e9 = 3/x
			paths.append(1)
		else:
			x = 6-x
			e9 = e9*x
			e9 = 7+e9
			paths.append(2)
		if j3 <= 5:
			j3 = j3*9
			paths.append(3)
		else:
			e9 = e9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))