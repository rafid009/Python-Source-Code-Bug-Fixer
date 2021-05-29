import numpy as np 

def function(x):

	n2 = 9
	x5 = 7
	paths = []
	try:
		if x <= 0:
			x = x/2
			x5 = 0-x5
			paths.append(1)
		else:
			x = 7/2
			x = n2+4
			x5 = 7-x5
			paths.append(2)
		if x >= 9:
			x5 = 0+x5
			x5 = x5-5
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		n2 = x5**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))