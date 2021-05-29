import numpy as np 

def function(x):

	p3 = 3
	g4 = x
	paths = []
	try:
		if p3 < 5:
			g4 = g4+8
			x = p3*x
			paths.append(1)
		else:
			g4 = 3*g4
			paths.append(2)
		if g4 < 6:
			p3 = p3-8
			x = 9-p3
			p3 = p3+p3
			paths.append(3)
		else:
			p3 = 2-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))