import numpy as np 

def function(x):

	n6 = x
	y8 = 6
	paths = []
	try:
		if n6 > 3:
			n6 = y8/n6
			paths.append(1)
		else:
			x = 3/7
			x = x+3
			n6 = 5*n6
			paths.append(2)
		if x <= 9:
			y8 = y8*7
			y8 = y8/n6
			y8 = y8-9
			paths.append(3)
		else:
			n6 = 3+1
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))