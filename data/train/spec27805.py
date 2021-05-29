import numpy as np 

def function(x):

	x8 = x
	n5 = 2
	paths = []
	try:
		if x8 < 5:
			x = x+5
			paths.append(1)
		else:
			x8 = 9*x
			n5 = 8-x8
			x8 = x8-4
			paths.append(2)
		if x <= 7:
			x8 = n5+x8
			x8 = x8-x8
			n5 = 4+n5
			paths.append(3)
		else:
			x8 = 4-x
			x8 = n5/x
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