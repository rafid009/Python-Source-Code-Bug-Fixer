import numpy as np 

def function(x):

	n6 = 0
	y3 = 1
	paths = []
	try:
		if x > 1:
			x = n6-4
			n6 = n6-7
			y3 = y3+5
			paths.append(1)
		else:
			y3 = y3/7
			n6 = n6*6
			n6 = n6*5
			paths.append(2)
		if y3 >= 8:
			x = 5*4
			y3 = y3*n6
			n6 = y3*n6
			paths.append(3)
		else:
			y3 = 7-x
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