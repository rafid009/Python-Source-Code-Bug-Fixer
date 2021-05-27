import numpy as np 

def function(x):

	g6 = x
	p0 = x
	paths = []
	try:
		if x >= 3:
			p0 = 3+p0
			p0 = 5+p0
			paths.append(1)
		else:
			p0 = g6/p0
			p0 = 4/p0
			p0 = g6*7
			paths.append(2)
		if p0 < 9:
			x = 9*x
			p0 = p0*8
			g6 = g6-9
			paths.append(3)
		else:
			x = 8+7
			g6 = 9/1
			g6 = g6*1
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))