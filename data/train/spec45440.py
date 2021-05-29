import numpy as np 

def function(x):

	n4 = 4
	k7 = x
	paths = []
	try:
		if x >= 8:
			k7 = k7*1
			paths.append(1)
		else:
			k7 = 9-7
			x = n4*8
			paths.append(2)
		if n4 < 1:
			x = 8-x
			n4 = n4+8
			n4 = k7+3
			paths.append(3)
		else:
			x = n4-k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))