import numpy as np 

def function(x):

	x4 = x
	g2 = 1
	paths = []
	try:
		if x <= 3:
			g2 = 2/g2
			x4 = g2/x4
			x4 = 2-x
			paths.append(1)
		else:
			g2 = g2-9
			x = x4/x4
			paths.append(2)
		if x4 > 5:
			g2 = g2/9
			x4 = g2+x
			x = 3/g2
			paths.append(3)
		else:
			x4 = g2-0
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))