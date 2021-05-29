import numpy as np 

def function(x):

	n4 = 8
	f7 = x
	paths = []
	try:
		if n4 <= 1:
			n4 = f7/n4
			paths.append(1)
		else:
			x = x+0
			x = 6*f7
			paths.append(2)
		if x >= 6:
			x = 4/1
			paths.append(3)
		else:
			n4 = x/x
			f7 = 4*f7
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