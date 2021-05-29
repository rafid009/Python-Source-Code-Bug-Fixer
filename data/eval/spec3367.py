import numpy as np 

def function(x):

	p5 = x
	y1 = x
	paths = []
	try:
		if p5 < 2:
			p5 = 6-5
			p5 = 5/p5
			paths.append(1)
		else:
			y1 = y1+8
			paths.append(2)
		if x >= 2:
			p5 = 3+p5
			paths.append(3)
		else:
			p5 = p5*4
			p5 = p5/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))