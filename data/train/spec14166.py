import numpy as np 

def function(x):

	y6 = 8
	p0 = x
	paths = []
	try:
		if p0 <= 2:
			y6 = y6/5
			paths.append(1)
		else:
			y6 = y6*2
			y6 = 7+y6
			paths.append(2)
		if p0 <= 6:
			y6 = 1+3
			x = x+4
			y6 = y6/8
			paths.append(3)
		else:
			x = x*3
			p0 = 3*p0
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