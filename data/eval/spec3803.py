import numpy as np 

def function(x):

	l8 = 0
	k1 = 7
	paths = []
	try:
		if l8 > 8:
			k1 = x/5
			x = x/x
			l8 = l8*l8
			paths.append(1)
		else:
			l8 = l8+7
			k1 = k1-x
			paths.append(2)
		if k1 > 1:
			x = 4-x
			l8 = l8-0
			k1 = 8*k1
			paths.append(3)
		else:
			l8 = 6-l8
			l8 = l8*9
			x = k1*6
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