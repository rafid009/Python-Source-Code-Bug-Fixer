import numpy as np 

def function(x):

	g8 = x
	u7 = x
	paths = []
	try:
		if u7 <= 5:
			g8 = 3-5
			paths.append(1)
		else:
			u7 = 6/6
			paths.append(2)
		if x <= 6:
			g8 = x+g8
			g8 = u7-g8
			paths.append(3)
		else:
			x = x+x
			x = 5+x
			g8 = 7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))