import numpy as np 

def function(x):

	p0 = x
	g5 = x
	x = x
	paths = []
	try:
		if x <= 6:
			p0 = x-4
			paths.append(1)
		else:
			x = x-x
			g5 = 3*g5
			g5 = 2/g5
			paths.append(2)
		if g5 >= 5:
			g5 = 2+6
			x = x*6
			p0 = 6-g5
			paths.append(3)
		else:
			g5 = g5*6
			x = x-8
			p0 = 4-p0
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