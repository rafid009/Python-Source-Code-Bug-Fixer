import numpy as np 

def function(x):

	g6 = x
	k5 = 8
	paths = []
	try:
		if g6 >= 7:
			x = k5+5
			x = 8/9
			x = x*g6
			paths.append(1)
		else:
			x = x-4
			k5 = g6/x
			k5 = 0+3
			paths.append(2)
		if x <= 2:
			g6 = 3-x
			g6 = g6-k5
			k5 = 9-k5
			paths.append(3)
		else:
			k5 = k5-8
			x = 3*0
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))