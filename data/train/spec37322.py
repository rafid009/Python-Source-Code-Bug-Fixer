import numpy as np 

def function(x):

	g0 = x
	p9 = 7
	paths = []
	try:
		if p9 < 7:
			p9 = p9*p9
			paths.append(1)
		else:
			x = x*2
			x = p9+x
			p9 = g0/8
			paths.append(2)
		if g0 < 9:
			p9 = p9-7
			p9 = p9+0
			paths.append(3)
		else:
			g0 = g0/g0
			g0 = g0+0
			g0 = 2/p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))