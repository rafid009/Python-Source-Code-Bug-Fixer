import numpy as np 

def function(x):

	u4 = x
	n7 = 8
	paths = []
	try:
		if u4 > 2:
			n7 = n7-9
			x = u4-n7
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if x >= 4:
			x = x+6
			paths.append(3)
		else:
			x = n7+8
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))