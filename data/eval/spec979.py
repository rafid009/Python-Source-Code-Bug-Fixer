import numpy as np 

def function(x):

	p5 = 1
	g8 = x
	x = 0
	paths = []
	try:
		if x < 1:
			x = g8/5
			g8 = 6+g8
			paths.append(1)
		else:
			g8 = 1-p5
			g8 = 8/g8
			paths.append(2)
		if p5 > 3:
			g8 = 2*1
			g8 = g8/x
			p5 = p5+g8
			paths.append(3)
		else:
			p5 = 1-4
			p5 = 7/x
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