import numpy as np 

def function(x):

	h2 = x
	n7 = x
	x = 8
	paths = []
	try:
		if n7 >= 6:
			h2 = 0*7
			paths.append(1)
		else:
			h2 = h2+n7
			paths.append(2)
		if x > 5:
			x = 5*4
			paths.append(3)
		else:
			h2 = h2-n7
			n7 = n7*6
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))