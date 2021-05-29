import numpy as np 

def function(x):

	n8 = x
	paths = []
	try:
		if x < 1:
			n8 = 3/8
			x = 2*3
			paths.append(1)
		else:
			n8 = 4*x
			paths.append(2)
		if n8 < 2:
			n8 = n8*n8
			x = n8+x
			paths.append(3)
		else:
			x = n8+6
			n8 = 4-n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))