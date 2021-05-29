import numpy as np 

def function(x):

	q6 = 1
	k7 = 8
	paths = []
	try:
		if q6 > 9:
			x = k7+k7
			paths.append(1)
		else:
			k7 = 6/k7
			x = x+8
			paths.append(2)
		if x >= 6:
			k7 = k7-4
			paths.append(3)
		else:
			k7 = 7+7
			k7 = q6/k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		q6 = k7**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))