import numpy as np 

def function(x):

	g8 = x
	p2 = 9
	paths = []
	try:
		if g8 > 7:
			g8 = g8-0
			paths.append(1)
		else:
			g8 = g8*0
			paths.append(2)
		if g8 >= 8:
			p2 = x-2
			x = x*6
			x = 7/6
			paths.append(3)
		else:
			g8 = 2-g8
			p2 = p2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))