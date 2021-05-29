import numpy as np 

def function(x):

	y3 = x
	n3 = 8
	paths = []
	try:
		if n3 <= 6:
			x = x/4
			y3 = 8/y3
			n3 = n3+7
			paths.append(1)
		else:
			n3 = 6*y3
			x = n3-x
			n3 = 3-n3
			paths.append(2)
		if y3 < 1:
			y3 = y3*6
			paths.append(3)
		else:
			n3 = 0-x
			n3 = 5/n3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))