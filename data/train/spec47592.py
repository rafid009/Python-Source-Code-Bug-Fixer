import numpy as np 

def function(x):

	p7 = x
	y0 = x
	paths = []
	try:
		if p7 < 9:
			x = 0/x
			x = x+p7
			paths.append(1)
		else:
			x = y0+5
			x = p7*7
			paths.append(2)
		if y0 < 3:
			y0 = x/y0
			x = x-x
			p7 = p7/9
			paths.append(3)
		else:
			y0 = y0+p7
			y0 = y0/4
			y0 = y0-8
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		y0 = p7**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))