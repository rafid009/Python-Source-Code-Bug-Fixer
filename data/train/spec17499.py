import numpy as np 

def function(x):

	l8 = 7
	g1 = x
	paths = []
	try:
		if l8 < 7:
			g1 = 2-g1
			x = 3-x
			paths.append(1)
		else:
			l8 = l8*6
			paths.append(2)
		if l8 > 3:
			l8 = l8+2
			paths.append(3)
		else:
			x = x/5
			g1 = 9-g1
			l8 = 5*l8
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))