import numpy as np 

def function(x):

	p9 = 4
	g0 = 2
	paths = []
	try:
		if g0 < 4:
			p9 = 5*8
			paths.append(1)
		else:
			g0 = 9-g0
			paths.append(2)
		if x > 8:
			g0 = 6+0
			paths.append(3)
		else:
			p9 = p9+7
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