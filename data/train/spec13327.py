import numpy as np 

def function(x):

	q6 = x
	j6 = x
	paths = []
	try:
		if q6 < 9:
			j6 = 8+j6
			j6 = 3-j6
			x = x-5
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x >= 2:
			x = 1-q6
			paths.append(3)
		else:
			x = 9*j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))