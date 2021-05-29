import numpy as np 

def function(x):

	k2 = 2
	n7 = 3
	paths = []
	try:
		if k2 <= 8:
			n7 = 7-2
			n7 = n7/x
			paths.append(1)
		else:
			k2 = 2-k2
			k2 = k2+5
			paths.append(2)
		if n7 < 2:
			n7 = n7-3
			n7 = n7/6
			paths.append(3)
		else:
			n7 = 5+x
			x = 9-x
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