import numpy as np 

def function(x):

	n8 = x
	x4 = x
	paths = []
	try:
		if x <= 3:
			n8 = x/1
			x4 = x4-x
			n8 = x4-1
			paths.append(1)
		else:
			n8 = 9+9
			n8 = n8*x4
			x4 = x4*7
			paths.append(2)
		if x4 > 1:
			x = x-4
			n8 = n8*1
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))