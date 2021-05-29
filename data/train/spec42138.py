import numpy as np 

def function(x):

	q6 = 3
	i1 = 3
	paths = []
	try:
		if x > 4:
			x = x+7
			paths.append(1)
		else:
			x = 4-x
			x = x-4
			paths.append(2)
		if x < 4:
			q6 = 5+q6
			i1 = i1-7
			paths.append(3)
		else:
			x = 5/6
			q6 = q6*9
			x = i1/x
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