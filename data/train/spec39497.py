import numpy as np 

def function(x):

	u2 = x
	g8 = 2
	paths = []
	try:
		if g8 < 4:
			u2 = 3-5
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if x > 9:
			g8 = 1/2
			x = x-1
			paths.append(3)
		else:
			g8 = x-x
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