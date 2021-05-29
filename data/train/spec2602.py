import numpy as np 

def function(x):

	a5 = x
	k7 = 2
	paths = []
	try:
		if x >= 1:
			x = 2+x
			paths.append(1)
		else:
			k7 = 3/x
			paths.append(2)
		if a5 > 4:
			x = x*x
			x = x/4
			x = x-0
			paths.append(3)
		else:
			x = k7-x
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