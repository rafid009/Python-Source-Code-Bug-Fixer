import numpy as np 

def function(x):

	y7 = 4
	g2 = 2
	paths = []
	try:
		if x > 5:
			g2 = g2*y7
			x = 8/4
			y7 = x+g2
			paths.append(1)
		else:
			g2 = g2*7
			paths.append(2)
		if g2 <= 0:
			y7 = y7*0
			g2 = 1-5
			g2 = 6-x
			paths.append(3)
		else:
			y7 = y7-0
			g2 = g2+y7
			y7 = 1*y7
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