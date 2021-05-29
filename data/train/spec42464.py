import numpy as np 

def function(x):

	q7 = x
	v3 = x
	paths = []
	try:
		if x > 0:
			v3 = 8/v3
			paths.append(1)
		else:
			x = x+3
			v3 = v3-9
			paths.append(2)
		if x >= 0:
			q7 = 5*q7
			paths.append(3)
		else:
			v3 = v3*q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))