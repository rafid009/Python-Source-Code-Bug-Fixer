import numpy as np 

def function(x):

	n3 = 9
	y8 = x
	paths = []
	try:
		if n3 > 4:
			n3 = x*n3
			paths.append(1)
		else:
			n3 = 5-y8
			y8 = 1/y8
			paths.append(2)
		if x >= 9:
			y8 = 0-y8
			n3 = 0-n3
			paths.append(3)
		else:
			x = 6-n3
			x = x/6
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))