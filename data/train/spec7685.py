import numpy as np 

def function(x):

	g7 = 3
	n5 = 8
	paths = []
	try:
		if n5 >= 2:
			n5 = n5+1
			n5 = n5+3
			paths.append(1)
		else:
			x = x+6
			n5 = 9-n5
			paths.append(2)
		if x <= 4:
			n5 = n5-3
			paths.append(3)
		else:
			x = g7*4
			g7 = g7-4
			n5 = n5*2
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))