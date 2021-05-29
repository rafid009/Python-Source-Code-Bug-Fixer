import numpy as np 

def function(x):

	l8 = x
	n5 = x
	paths = []
	try:
		if x >= 0:
			x = x/6
			x = x+3
			paths.append(1)
		else:
			l8 = l8/6
			x = x/7
			l8 = 8-l8
			paths.append(2)
		if n5 >= 5:
			x = 3-x
			n5 = n5/x
			paths.append(3)
		else:
			n5 = 4-n5
			n5 = x+l8
			n5 = 8+x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))