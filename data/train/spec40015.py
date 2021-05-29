import numpy as np 

def function(x):

	p5 = x
	g8 = x
	paths = []
	try:
		if g8 <= 9:
			x = x*3
			x = p5/x
			paths.append(1)
		else:
			p5 = p5/4
			p5 = p5+0
			g8 = g8/8
			paths.append(2)
		if g8 > 7:
			x = x-4
			paths.append(3)
		else:
			x = 0-x
			x = x+1
			x = 8-g8
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