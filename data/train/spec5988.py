import numpy as np 

def function(x):

	g2 = 7
	y1 = x
	paths = []
	try:
		if y1 >= 8:
			y1 = 8/7
			y1 = y1*4
			paths.append(1)
		else:
			x = 3+x
			g2 = g2/2
			paths.append(2)
		if g2 < 4:
			y1 = y1*3
			x = 1*x
			g2 = g2+x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))