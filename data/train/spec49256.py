import numpy as np 

def function(x):

	y2 = x
	n2 = 4
	paths = []
	try:
		if n2 < 0:
			x = x/y2
			y2 = x-y2
			x = x*n2
			paths.append(1)
		else:
			n2 = n2+5
			paths.append(2)
		if n2 > 5:
			n2 = n2*6
			x = 2+x
			paths.append(3)
		else:
			x = 7-5
			n2 = n2/x
			n2 = x*n2
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