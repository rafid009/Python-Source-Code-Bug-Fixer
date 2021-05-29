import numpy as np 

def function(x):

	g5 = 1
	p7 = 3
	paths = []
	try:
		if x <= 1:
			p7 = 0-p7
			p7 = x-7
			g5 = p7*6
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if p7 >= 1:
			x = 8*1
			x = x*6
			g5 = g5/4
			paths.append(3)
		else:
			g5 = g5-0
			p7 = p7+6
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))