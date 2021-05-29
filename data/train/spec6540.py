import numpy as np 

def function(x):

	x5 = 9
	j0 = 4
	paths = []
	try:
		if x <= 1:
			x = x-8
			j0 = j0*5
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if j0 <= 7:
			j0 = j0-0
			x5 = x5-8
			paths.append(3)
		else:
			j0 = 5+x
			x5 = 1-x5
			j0 = j0+7
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		j0 = x5**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))