import numpy as np 

def function(x):

	y2 = x
	n0 = 3
	paths = []
	try:
		if y2 < 5:
			x = y2-x
			x = 0-9
			x = x*1
			paths.append(1)
		else:
			x = y2*n0
			x = x/x
			n0 = n0/5
			paths.append(2)
		if x < 7:
			y2 = x/y2
			y2 = y2/3
			x = y2/x
			paths.append(3)
		else:
			n0 = n0*y2
			n0 = x-5
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))