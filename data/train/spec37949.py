import numpy as np 

def function(x):

	y6 = x
	n9 = 7
	paths = []
	try:
		if y6 > 9:
			y6 = y6-4
			paths.append(1)
		else:
			y6 = 8-y6
			y6 = y6*5
			paths.append(2)
		if x <= 7:
			x = 3/x
			n9 = n9+8
			y6 = 6*y6
			paths.append(3)
		else:
			n9 = n9-x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		y6 = n9**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))