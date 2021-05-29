import numpy as np 

def function(x):

	y1 = 8
	n9 = 9
	paths = []
	try:
		if y1 <= 2:
			x = n9*x
			y1 = y1*8
			paths.append(1)
		else:
			n9 = 8*2
			paths.append(2)
		if x <= 9:
			n9 = n9-n9
			x = x-2
			n9 = n9-x
			paths.append(3)
		else:
			n9 = n9+n9
			y1 = y1*y1
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		y1 = n9**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))