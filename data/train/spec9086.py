import numpy as np 

def function(x):

	g4 = x
	p3 = 6
	paths = []
	try:
		if p3 <= 8:
			p3 = 8*x
			x = 9-p3
			paths.append(1)
		else:
			g4 = x/6
			x = x*0
			x = x-x
			paths.append(2)
		if x > 6:
			g4 = g4*g4
			g4 = 2*g4
			paths.append(3)
		else:
			g4 = x+x
			p3 = p3-x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		g4 = p3**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))