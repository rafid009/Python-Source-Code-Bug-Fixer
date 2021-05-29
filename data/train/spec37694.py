import numpy as np 

def function(x):

	p1 = 4
	y1 = 5
	paths = []
	try:
		if y1 < 2:
			y1 = 6/1
			y1 = x+y1
			p1 = 8-x
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if x >= 4:
			p1 = 6/2
			y1 = p1/p1
			paths.append(3)
		else:
			p1 = p1/p1
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