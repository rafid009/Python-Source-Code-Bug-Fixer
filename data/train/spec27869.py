import numpy as np 

def function(x):

	p0 = 2
	g9 = 6
	x = x
	paths = []
	try:
		if g9 < 0:
			x = x/x
			p0 = 2-p0
			paths.append(1)
		else:
			g9 = g9+x
			x = x*8
			paths.append(2)
		if x < 7:
			g9 = p0-8
			paths.append(3)
		else:
			x = g9-g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))