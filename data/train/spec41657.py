import numpy as np 

def function(x):

	g0 = 7
	k5 = 9
	paths = []
	try:
		if x < 4:
			x = 4+7
			k5 = 0+g0
			k5 = 8*k5
			paths.append(1)
		else:
			x = 7-x
			x = 0+x
			k5 = 7*k5
			paths.append(2)
		if g0 < 0:
			g0 = g0/x
			paths.append(3)
		else:
			x = 8+x
			k5 = k5+x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))