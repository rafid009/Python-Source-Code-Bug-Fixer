import numpy as np 

def function(x):

	g5 = 9
	p7 = x
	x = 3
	paths = []
	try:
		if p7 > 7:
			p7 = p7-0
			paths.append(1)
		else:
			x = p7-0
			g5 = g5/8
			x = x-7
			paths.append(2)
		if x > 5:
			p7 = 3*p7
			paths.append(3)
		else:
			p7 = 5+p7
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