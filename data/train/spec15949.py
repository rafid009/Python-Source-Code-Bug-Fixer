import numpy as np 

def function(x):

	p1 = 5
	g1 = 6
	paths = []
	try:
		if x >= 0:
			p1 = 0-3
			p1 = x+4
			x = 7-p1
			paths.append(1)
		else:
			g1 = p1+9
			paths.append(2)
		if g1 <= 6:
			p1 = 9/x
			p1 = p1/6
			paths.append(3)
		else:
			p1 = p1+9
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