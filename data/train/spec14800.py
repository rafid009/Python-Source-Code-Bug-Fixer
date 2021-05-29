import numpy as np 

def function(x):

	g2 = 0
	q7 = 4
	paths = []
	try:
		if x <= 2:
			q7 = q7-x
			q7 = q7/8
			x = x/7
			paths.append(1)
		else:
			q7 = q7*0
			q7 = x-8
			paths.append(2)
		if q7 < 0:
			g2 = x-g2
			g2 = g2+q7
			paths.append(3)
		else:
			g2 = 4*g2
			x = x+2
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