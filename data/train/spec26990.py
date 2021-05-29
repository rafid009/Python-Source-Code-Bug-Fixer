import numpy as np 

def function(x):

	g2 = 8
	q7 = x
	x = 4
	paths = []
	try:
		if q7 < 3:
			x = q7/9
			paths.append(1)
		else:
			x = x-0
			g2 = 9*2
			paths.append(2)
		if x > 3:
			x = x+8
			q7 = g2/4
			g2 = q7/2
			paths.append(3)
		else:
			g2 = g2-1
			x = 9*6
			x = x+g2
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		g2 = q7**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))