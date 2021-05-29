import numpy as np 

def function(x):

	p3 = 8
	g4 = x
	x = 5
	paths = []
	try:
		if p3 > 9:
			p3 = 5*p3
			g4 = 6+g4
			p3 = 3-g4
			paths.append(1)
		else:
			p3 = p3*3
			x = x-x
			paths.append(2)
		if g4 >= 9:
			x = 2-g4
			x = 5-8
			paths.append(3)
		else:
			x = x-3
			g4 = 1/p3
			p3 = 8+p3
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