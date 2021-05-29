import numpy as np 

def function(x):

	j0 = 1
	q7 = x
	paths = []
	try:
		if j0 >= 6:
			j0 = j0/4
			paths.append(1)
		else:
			q7 = j0+0
			q7 = 0/q7
			paths.append(2)
		if q7 > 6:
			q7 = q7/7
			q7 = 5+x
			x = 9-1
			paths.append(3)
		else:
			j0 = j0+j0
			j0 = x+0
			x = 5+x
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