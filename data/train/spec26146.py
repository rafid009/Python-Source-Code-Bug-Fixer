import numpy as np 

def function(x):

	n3 = x
	y4 = 3
	paths = []
	try:
		if x >= 3:
			y4 = 2/y4
			n3 = 2/x
			n3 = n3/y4
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if n3 > 0:
			n3 = 9+n3
			paths.append(3)
		else:
			y4 = y4-5
			n3 = n3*0
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		n3 = y4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))