import numpy as np 

def function(x):

	n4 = 9
	x8 = x
	paths = []
	try:
		if n4 > 9:
			x = x*2
			paths.append(1)
		else:
			x8 = 9+x8
			x = x*x8
			paths.append(2)
		if n4 >= 6:
			n4 = x8-x
			paths.append(3)
		else:
			n4 = n4*2
			x8 = n4-0
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))