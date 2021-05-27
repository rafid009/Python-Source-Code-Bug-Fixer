import numpy as np 

def function(x):

	y0 = 6
	p5 = 8
	paths = []
	try:
		if x < 2:
			y0 = x*5
			p5 = p5-1
			paths.append(1)
		else:
			p5 = p5*2
			paths.append(2)
		if p5 > 4:
			p5 = 3/y0
			paths.append(3)
		else:
			y0 = 0+y0
			y0 = 8+8
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))