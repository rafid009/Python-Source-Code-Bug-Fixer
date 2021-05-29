import numpy as np 

def function(x):

	n6 = x
	g8 = 6
	x = 4
	paths = []
	try:
		if x >= 1:
			n6 = 9*n6
			n6 = 4*n6
			x = x-x
			paths.append(1)
		else:
			g8 = x+x
			x = n6-n6
			n6 = 2+2
			paths.append(2)
		if x < 0:
			n6 = n6+2
			x = x/1
			paths.append(3)
		else:
			x = x/3
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