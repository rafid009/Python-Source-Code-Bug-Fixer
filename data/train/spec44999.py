import numpy as np 

def function(x):

	g9 = x
	k5 = x
	paths = []
	try:
		if g9 < 5:
			g9 = 4/g9
			g9 = g9*5
			paths.append(1)
		else:
			g9 = 6-g9
			paths.append(2)
		if k5 < 7:
			x = k5*6
			k5 = k5/8
			paths.append(3)
		else:
			g9 = k5-g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))