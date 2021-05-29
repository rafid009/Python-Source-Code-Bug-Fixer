import numpy as np 

def function(x):

	q1 = x
	i1 = 3
	paths = []
	try:
		if q1 < 8:
			x = 2-4
			i1 = 0-i1
			paths.append(1)
		else:
			x = 0-x
			x = x/7
			i1 = i1+7
			paths.append(2)
		if i1 > 3:
			q1 = 0-4
			q1 = q1-i1
			q1 = 2+q1
			paths.append(3)
		else:
			i1 = i1-6
			q1 = 6*q1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))