import numpy as np 

def function(x):

	p1 = 1
	g4 = x
	paths = []
	try:
		if g4 > 7:
			p1 = 8/x
			p1 = p1+4
			x = g4-x
			paths.append(1)
		else:
			g4 = g4*x
			p1 = p1/7
			g4 = g4/2
			paths.append(2)
		if g4 < 4:
			p1 = 1/3
			x = x-5
			paths.append(3)
		else:
			p1 = p1/4
			p1 = 2+p1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))