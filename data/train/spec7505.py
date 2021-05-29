import numpy as np 

def function(x):

	g5 = 5
	x8 = x
	paths = []
	try:
		if x8 < 4:
			g5 = x*8
			x = x/x
			paths.append(1)
		else:
			x8 = x8/g5
			paths.append(2)
		if x > 0:
			g5 = g5/6
			paths.append(3)
		else:
			x8 = x8-8
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))