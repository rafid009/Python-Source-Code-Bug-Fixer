import numpy as np 

def function(x):

	y3 = 5
	n8 = x
	paths = []
	try:
		if n8 >= 7:
			x = x-n8
			n8 = 3-n8
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if y3 > 3:
			x = 3*y3
			paths.append(3)
		else:
			x = 3-8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))