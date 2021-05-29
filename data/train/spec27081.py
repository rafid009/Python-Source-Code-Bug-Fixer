import numpy as np 

def function(x):

	x6 = 1
	n3 = 4
	paths = []
	try:
		if n3 > 2:
			x = x-n3
			paths.append(1)
		else:
			x = n3/3
			paths.append(2)
		if x > 8:
			x = 7-0
			paths.append(3)
		else:
			x = x/7
			x6 = 8/x6
			x6 = n3/x6
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