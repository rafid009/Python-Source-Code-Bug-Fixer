import numpy as np 

def function(x):

	j0 = 9
	j4 = 0
	paths = []
	try:
		if j0 < 5:
			j4 = j4-6
			paths.append(1)
		else:
			j4 = j4/j0
			paths.append(2)
		if j4 > 5:
			j4 = 1/x
			j4 = j4+9
			j4 = 8/j4
			paths.append(3)
		else:
			x = x+4
			x = x-j4
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