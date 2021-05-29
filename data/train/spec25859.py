import numpy as np 

def function(x):

	i1 = 6
	q6 = x
	paths = []
	try:
		if q6 >= 1:
			i1 = q6/1
			paths.append(1)
		else:
			q6 = q6/9
			x = 4+7
			q6 = 5+0
			paths.append(2)
		if i1 < 0:
			q6 = 3+8
			x = 6*x
			i1 = 1-i1
			paths.append(3)
		else:
			q6 = 0-2
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))