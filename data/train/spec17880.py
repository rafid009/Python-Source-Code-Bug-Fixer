import numpy as np 

def function(x):

	g6 = x
	k5 = x
	paths = []
	try:
		if g6 < 2:
			x = k5-1
			x = x/8
			k5 = 5/k5
			paths.append(1)
		else:
			g6 = 3-g6
			g6 = 9+g6
			g6 = g6/7
			paths.append(2)
		if x < 3:
			x = 3+x
			paths.append(3)
		else:
			x = 6+0
			k5 = k5/k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))