import numpy as np 

def function(x):

	i6 = 4
	q3 = x
	paths = []
	try:
		if x >= 3:
			q3 = 4*q3
			paths.append(1)
		else:
			i6 = 0-2
			paths.append(2)
		if x > 1:
			x = x*q3
			paths.append(3)
		else:
			q3 = 6*8
			q3 = q3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))