import numpy as np 

def function(x):

	e2 = 3
	j0 = x
	paths = []
	try:
		if x >= 9:
			j0 = 4/x
			e2 = e2*1
			paths.append(1)
		else:
			j0 = j0/x
			j0 = j0-1
			e2 = e2+9
			paths.append(2)
		if j0 <= 6:
			j0 = e2*4
			paths.append(3)
		else:
			e2 = 0*e2
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