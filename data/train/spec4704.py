import numpy as np 

def function(x):

	n4 = x
	w2 = 2
	paths = []
	try:
		if x >= 0:
			w2 = w2/w2
			x = x/w2
			paths.append(1)
		else:
			n4 = n4*8
			paths.append(2)
		if n4 > 6:
			n4 = 3+n4
			n4 = 6-3
			x = x+2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))