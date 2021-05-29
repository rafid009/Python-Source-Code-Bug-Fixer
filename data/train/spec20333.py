import numpy as np 

def function(x):

	a3 = 4
	j0 = 4
	paths = []
	try:
		if x < 6:
			j0 = x-x
			j0 = 6+j0
			x = 9+x
			paths.append(1)
		else:
			a3 = 6+9
			paths.append(2)
		if a3 <= 3:
			x = 7-x
			x = 6/x
			x = x/x
			paths.append(3)
		else:
			a3 = 7*6
			j0 = 4-3
			j0 = j0*j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))