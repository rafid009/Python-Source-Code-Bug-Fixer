import numpy as np 

def function(x):

	i4 = 6
	q8 = 8
	paths = []
	try:
		if x <= 5:
			x = x/9
			paths.append(1)
		else:
			x = 6*x
			q8 = 9-1
			paths.append(2)
		if q8 <= 2:
			q8 = 7+i4
			paths.append(3)
		else:
			i4 = x+6
			q8 = q8/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))