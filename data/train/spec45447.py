import numpy as np 

def function(x):

	n5 = x
	g9 = 3
	paths = []
	try:
		if x < 7:
			x = x-4
			g9 = g9*n5
			paths.append(1)
		else:
			g9 = 7/g9
			n5 = n5*5
			paths.append(2)
		if g9 >= 9:
			n5 = 7/n5
			paths.append(3)
		else:
			x = 6*1
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