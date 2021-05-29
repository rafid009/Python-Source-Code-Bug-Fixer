import numpy as np 

def function(x):

	x5 = x
	k5 = 1
	paths = []
	try:
		if x5 < 5:
			x = x*x
			k5 = 2/x
			paths.append(1)
		else:
			k5 = x+8
			paths.append(2)
		if x5 <= 7:
			x5 = 6-x5
			paths.append(3)
		else:
			x = x/x
			k5 = x5+5
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))