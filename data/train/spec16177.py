import numpy as np 

def function(x):

	l3 = x
	y0 = x
	paths = []
	try:
		if x < 0:
			x = x*x
			y0 = y0/4
			paths.append(1)
		else:
			y0 = y0-y0
			l3 = y0*l3
			paths.append(2)
		if x > 6:
			x = y0+x
			x = l3/x
			x = 2-x
			paths.append(3)
		else:
			l3 = l3+8
			y0 = x*l3
			x = l3-0
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))