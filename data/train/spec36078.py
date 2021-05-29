import numpy as np 

def function(x):

	p5 = 3
	g6 = 6
	paths = []
	try:
		if p5 >= 7:
			g6 = 5/x
			p5 = 8/9
			p5 = 0*g6
			paths.append(1)
		else:
			g6 = g6+g6
			x = x*g6
			x = x-g6
			paths.append(2)
		if x > 2:
			x = p5+x
			g6 = g6+9
			x = 2+x
			paths.append(3)
		else:
			g6 = 9+g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))