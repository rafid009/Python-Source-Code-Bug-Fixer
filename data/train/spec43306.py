import numpy as np 

def function(x):

	y2 = 9
	n0 = 7
	paths = []
	try:
		if n0 > 2:
			y2 = y2/7
			n0 = n0-1
			n0 = n0+2
			paths.append(1)
		else:
			n0 = n0*n0
			n0 = n0/9
			y2 = y2-n0
			paths.append(2)
		if y2 >= 9:
			x = 0+y2
			paths.append(3)
		else:
			x = 5+x
			x = 7*2
			y2 = 1-y2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))