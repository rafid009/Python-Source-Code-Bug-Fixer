import numpy as np 

def function(x):

	n3 = x
	y8 = x
	x = 1
	paths = []
	try:
		if n3 <= 2:
			x = y8*5
			n3 = n3-6
			y8 = y8-8
			paths.append(1)
		else:
			n3 = x/3
			n3 = n3-n3
			paths.append(2)
		if n3 > 3:
			n3 = n3*n3
			paths.append(3)
		else:
			x = x-n3
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