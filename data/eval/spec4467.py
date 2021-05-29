import numpy as np 

def function(x):

	l8 = x
	k6 = x
	x = x
	paths = []
	try:
		if x >= 4:
			l8 = l8/1
			k6 = k6/1
			l8 = l8-9
			paths.append(1)
		else:
			x = x+x
			l8 = l8-k6
			paths.append(2)
		if x >= 7:
			l8 = l8-k6
			paths.append(3)
		else:
			x = l8-x
			l8 = k6+l8
			l8 = l8+7
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