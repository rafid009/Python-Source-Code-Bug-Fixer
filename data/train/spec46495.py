import numpy as np 

def function(x):

	a6 = x
	g2 = 2
	paths = []
	try:
		if g2 < 1:
			a6 = 4+5
			g2 = a6-g2
			g2 = g2*2
			paths.append(1)
		else:
			x = 0-1
			paths.append(2)
		if x <= 5:
			g2 = 3*7
			paths.append(3)
		else:
			g2 = x-g2
			x = 6-6
			a6 = a6*1
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))