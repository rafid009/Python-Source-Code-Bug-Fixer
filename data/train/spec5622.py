import numpy as np 

def function(x):

	g9 = 4
	n5 = 0
	x = 7
	paths = []
	try:
		if g9 > 7:
			n5 = n5-3
			g9 = 4+1
			g9 = g9+9
			paths.append(1)
		else:
			n5 = 5+n5
			paths.append(2)
		if g9 > 2:
			n5 = 1-6
			paths.append(3)
		else:
			n5 = n5+8
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))