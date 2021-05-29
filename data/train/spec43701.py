import numpy as np 

def function(x):

	p8 = 2
	y0 = 7
	paths = []
	try:
		if p8 <= 1:
			y0 = 8-y0
			paths.append(1)
		else:
			x = x*p8
			p8 = 4-2
			paths.append(2)
		if x > 9:
			y0 = 6-y0
			p8 = 1-9
			p8 = p8+9
			paths.append(3)
		else:
			y0 = y0/4
			p8 = 2+7
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