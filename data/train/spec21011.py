import numpy as np 

def function(x):

	y2 = x
	n8 = x
	paths = []
	try:
		if n8 > 3:
			n8 = 8/6
			paths.append(1)
		else:
			n8 = 6*x
			y2 = 9/y2
			paths.append(2)
		if n8 <= 9:
			n8 = n8+7
			n8 = 4*n8
			paths.append(3)
		else:
			n8 = 2+x
			n8 = x+4
			x = 7/n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))