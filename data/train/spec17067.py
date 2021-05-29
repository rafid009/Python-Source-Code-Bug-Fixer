import numpy as np 

def function(x):

	k7 = 0
	x0 = x
	paths = []
	try:
		if k7 > 0:
			x0 = x0+k7
			paths.append(1)
		else:
			k7 = k7+x0
			paths.append(2)
		if x0 >= 4:
			x0 = x0/x
			x0 = k7-5
			k7 = x0+3
			paths.append(3)
		else:
			x0 = x/x0
			x = 4/x
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