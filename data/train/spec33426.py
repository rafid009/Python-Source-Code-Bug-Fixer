import numpy as np 

def function(x):

	p8 = x
	y2 = x
	paths = []
	try:
		if x > 4:
			p8 = 0*p8
			p8 = p8*6
			x = x*4
			paths.append(1)
		else:
			x = p8-1
			paths.append(2)
		if y2 <= 7:
			x = y2-4
			y2 = x*y2
			x = 0+p8
			paths.append(3)
		else:
			y2 = p8/x
			p8 = y2/x
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