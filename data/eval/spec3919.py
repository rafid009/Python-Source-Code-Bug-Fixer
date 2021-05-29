import numpy as np 

def function(x):

	y0 = x
	p3 = x
	paths = []
	try:
		if p3 > 8:
			x = 9+7
			p3 = y0+7
			y0 = y0-p3
			paths.append(1)
		else:
			p3 = p3+9
			p3 = 4*p3
			paths.append(2)
		if x < 5:
			x = 8/x
			y0 = y0*1
			p3 = 1/p3
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		p3 = y0**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))