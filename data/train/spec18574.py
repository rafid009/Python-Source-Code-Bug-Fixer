import numpy as np 

def function(x):

	i6 = x
	q3 = 0
	paths = []
	try:
		if x < 7:
			i6 = 4+2
			q3 = 0*6
			q3 = i6*q3
			paths.append(1)
		else:
			i6 = i6+2
			paths.append(2)
		if x >= 5:
			q3 = q3+2
			paths.append(3)
		else:
			q3 = q3+0
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