import numpy as np 

def function(x):

	k7 = x
	x2 = 1
	paths = []
	try:
		if x2 > 3:
			k7 = k7-1
			paths.append(1)
		else:
			x2 = x2-8
			paths.append(2)
		if k7 < 7:
			x = x-k7
			paths.append(3)
		else:
			x2 = 4/x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))