import numpy as np 

def function(x):

	x5 = 8
	x2 = x
	paths = []
	try:
		if x >= 7:
			x2 = 8-x2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x5 < 5:
			x = x/1
			paths.append(3)
		else:
			x5 = x5+7
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))