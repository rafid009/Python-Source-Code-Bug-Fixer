import numpy as np 

def function(x):

	x6 = x
	n5 = x
	x = 5
	paths = []
	try:
		if x6 >= 0:
			x = x-8
			x6 = x6*n5
			paths.append(1)
		else:
			x6 = x+x6
			n5 = n5*7
			paths.append(2)
		if n5 < 8:
			x6 = n5-x6
			n5 = 6/x
			x = 2-x6
			paths.append(3)
		else:
			x = 3+n5
			x6 = n5-8
			x6 = 0-x6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x6 = n5**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))