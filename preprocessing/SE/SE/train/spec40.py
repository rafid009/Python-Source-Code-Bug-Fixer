import numpy as np 

def function(x):

	y8 = 4
	n3 = 2
	paths = []
	try:
		if x > 0:
			n3 = n3-0
			paths.append(1)
		else:
			y8 = 4/x
			n3 = 0-5
			y8 = y8/x
			paths.append(2)
		if n3 <= 4:
			y8 = 1*n3
			paths.append(3)
		else:
			y8 = 9*5
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		y8 = n3**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))