import numpy as np 

def function(x):

	y4 = 4
	j0 = 0
	paths = []
	try:
		if x > 1:
			y4 = 9-y4
			y4 = x/4
			paths.append(1)
		else:
			j0 = j0-x
			paths.append(2)
		if x <= 6:
			y4 = y4-1
			paths.append(3)
		else:
			j0 = y4+j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		y4 = j0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))