import numpy as np 

def function(x):

	a1 = 5
	x2 = x
	paths = []
	try:
		if x > 2:
			x2 = x2+x2
			x = 0-x
			x2 = x2/3
			paths.append(1)
		else:
			a1 = x2-a1
			x = 5/x
			paths.append(2)
		if a1 > 0:
			x2 = x2+x
			a1 = 5+3
			x2 = 7-1
			paths.append(3)
		else:
			x = 9+x
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