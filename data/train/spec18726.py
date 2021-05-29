import numpy as np 

def function(x):

	l7 = x
	i4 = 3
	paths = []
	try:
		if x <= 1:
			i4 = i4-i4
			x = 8-i4
			i4 = 1+4
			paths.append(1)
		else:
			l7 = l7/7
			x = x-0
			x = 5*x
			paths.append(2)
		if x >= 2:
			x = x-4
			paths.append(3)
		else:
			i4 = 3-5
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))