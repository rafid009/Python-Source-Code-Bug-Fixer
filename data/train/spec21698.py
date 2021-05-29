import numpy as np 

def function(x):

	g7 = 1
	p5 = 4
	paths = []
	try:
		if x <= 0:
			x = x-p5
			paths.append(1)
		else:
			p5 = p5*3
			paths.append(2)
		if x >= 7:
			p5 = 6-p5
			x = x+3
			paths.append(3)
		else:
			p5 = p5-9
			g7 = g7+4
			p5 = 4-2
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