import numpy as np 

def function(x):

	j0 = 5
	j5 = 7
	paths = []
	try:
		if x >= 0:
			j5 = j0+7
			j5 = 6/j0
			paths.append(1)
		else:
			j5 = 1/j5
			j5 = x+0
			paths.append(2)
		if j0 <= 9:
			x = x+3
			paths.append(3)
		else:
			j0 = j0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))