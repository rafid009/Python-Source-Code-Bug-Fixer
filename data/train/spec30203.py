import numpy as np 

def function(x):

	u7 = x
	n0 = x
	paths = []
	try:
		if u7 < 9:
			n0 = 5/2
			paths.append(1)
		else:
			u7 = u7-9
			u7 = u7/2
			paths.append(2)
		if x <= 7:
			n0 = n0-1
			x = x-3
			paths.append(3)
		else:
			x = 0+x
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