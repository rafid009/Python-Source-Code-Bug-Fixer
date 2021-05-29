import numpy as np 

def function(x):

	k1 = x
	l7 = 9
	paths = []
	try:
		if x < 0:
			k1 = k1+k1
			l7 = 4-7
			k1 = k1-4
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x < 1:
			l7 = l7/7
			l7 = l7/1
			k1 = k1*9
			paths.append(3)
		else:
			l7 = 4+l7
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