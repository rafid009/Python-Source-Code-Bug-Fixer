import numpy as np 

def function(x):

	x5 = x
	j0 = x
	paths = []
	try:
		if x5 <= 6:
			x = 0+x
			paths.append(1)
		else:
			j0 = j0-x5
			x = x5+x
			x5 = x5+9
			paths.append(2)
		if x5 > 7:
			x5 = 7*j0
			j0 = j0+j0
			paths.append(3)
		else:
			x5 = j0+x5
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