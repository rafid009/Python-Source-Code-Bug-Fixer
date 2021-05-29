import numpy as np 

def function(x):

	u2 = x
	g8 = 3
	paths = []
	try:
		if g8 > 4:
			x = x+9
			g8 = 2/g8
			x = x-g8
			paths.append(1)
		else:
			x = x+7
			g8 = g8/1
			x = g8/x
			paths.append(2)
		if x > 6:
			x = x+7
			paths.append(3)
		else:
			u2 = 7*u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))