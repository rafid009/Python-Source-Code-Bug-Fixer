import numpy as np 

def function(x):

	l6 = x
	y7 = x
	paths = []
	try:
		if x >= 6:
			y7 = 1*3
			paths.append(1)
		else:
			y7 = y7+2
			y7 = y7/y7
			paths.append(2)
		if l6 < 7:
			y7 = y7/y7
			x = 4/x
			l6 = 4/l6
			paths.append(3)
		else:
			y7 = y7-8
			y7 = 9*8
			x = x+8
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		y7 = l6**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))