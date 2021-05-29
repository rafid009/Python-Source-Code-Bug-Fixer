import numpy as np 

def function(x):

	n0 = 7
	x6 = 3
	paths = []
	try:
		if x6 > 0:
			n0 = 8/x6
			x = x/7
			paths.append(1)
		else:
			x6 = x6-9
			x = 5/n0
			n0 = n0-0
			paths.append(2)
		if x < 4:
			n0 = n0/4
			n0 = 7/n0
			x6 = n0-1
			paths.append(3)
		else:
			x6 = x6/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))