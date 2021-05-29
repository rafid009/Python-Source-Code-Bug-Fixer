import numpy as np 

def function(x):

	l0 = 8
	y4 = 8
	paths = []
	try:
		if l0 >= 8:
			x = x-5
			y4 = y4/y4
			paths.append(1)
		else:
			l0 = l0/y4
			y4 = x/l0
			l0 = 4+l0
			paths.append(2)
		if y4 >= 3:
			l0 = l0*l0
			y4 = y4+l0
			paths.append(3)
		else:
			l0 = 8/l0
			l0 = l0/4
			l0 = l0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))