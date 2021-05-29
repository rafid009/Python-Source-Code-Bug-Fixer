import numpy as np 

def function(x):

	y2 = 1
	n0 = x
	paths = []
	try:
		if x < 4:
			y2 = x*y2
			n0 = 5/2
			paths.append(1)
		else:
			x = 4*x
			y2 = n0+y2
			paths.append(2)
		if n0 > 9:
			n0 = n0/n0
			y2 = y2-1
			y2 = 5-n0
			paths.append(3)
		else:
			x = 8-3
			y2 = y2+2
			x = y2/y2
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