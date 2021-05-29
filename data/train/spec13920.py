import numpy as np 

def function(x):

	g2 = 5
	q9 = 2
	paths = []
	try:
		if q9 >= 0:
			g2 = g2+1
			x = 4*x
			paths.append(1)
		else:
			q9 = 6/q9
			x = x+4
			paths.append(2)
		if q9 < 4:
			q9 = 2-3
			g2 = g2+7
			paths.append(3)
		else:
			g2 = 2-g2
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))