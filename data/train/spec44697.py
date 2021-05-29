import numpy as np 

def function(x):

	y0 = 5
	n4 = x
	paths = []
	try:
		if n4 <= 4:
			x = 1/x
			x = 5+7
			paths.append(1)
		else:
			n4 = 7-n4
			paths.append(2)
		if y0 <= 0:
			y0 = y0/4
			n4 = n4+1
			paths.append(3)
		else:
			n4 = x/n4
			n4 = 2-n4
			n4 = 2+n4
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