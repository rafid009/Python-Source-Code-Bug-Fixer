import numpy as np 

def function(x):

	l0 = 4
	x6 = x
	paths = []
	try:
		if l0 < 1:
			l0 = l0-0
			paths.append(1)
		else:
			x = l0/x6
			x6 = 5/x
			paths.append(2)
		if x > 8:
			x6 = x6*6
			paths.append(3)
		else:
			l0 = l0+l0
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))