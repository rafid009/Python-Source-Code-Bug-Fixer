import numpy as np 

def function(x):

	q3 = x
	x3 = 2
	paths = []
	try:
		if q3 < 5:
			x3 = x3+1
			paths.append(1)
		else:
			x3 = 2/1
			paths.append(2)
		if q3 > 8:
			x3 = x3+7
			paths.append(3)
		else:
			x3 = x3+x3
			q3 = 9*9
			x = x3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))