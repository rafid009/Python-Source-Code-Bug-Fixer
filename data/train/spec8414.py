import numpy as np 

def function(x):

	n3 = x
	k5 = 3
	paths = []
	try:
		if n3 < 0:
			k5 = k5/3
			x = 8/x
			n3 = n3-x
			paths.append(1)
		else:
			k5 = k5+0
			k5 = n3/4
			n3 = n3*8
			paths.append(2)
		if n3 <= 8:
			k5 = k5/x
			n3 = 1-n3
			paths.append(3)
		else:
			n3 = n3/7
			n3 = 1/n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))