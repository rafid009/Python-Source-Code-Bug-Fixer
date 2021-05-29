import numpy as np 

def function(x):

	y1 = 0
	l8 = x
	paths = []
	try:
		if l8 > 3:
			y1 = 3*y1
			l8 = l8+9
			paths.append(1)
		else:
			y1 = y1*3
			paths.append(2)
		if l8 >= 6:
			l8 = l8+x
			paths.append(3)
		else:
			y1 = y1-1
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		y1 = l8**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))