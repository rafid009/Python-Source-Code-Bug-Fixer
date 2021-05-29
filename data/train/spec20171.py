import numpy as np 

def function(x):

	g9 = 7
	k7 = 6
	paths = []
	try:
		if x < 5:
			k7 = k7-7
			paths.append(1)
		else:
			k7 = k7-5
			g9 = g9+5
			g9 = g9+g9
			paths.append(2)
		if k7 < 7:
			x = x+g9
			paths.append(3)
		else:
			x = 1/7
			g9 = g9*4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))