import numpy as np 

def function(x):

	y1 = 5
	p1 = 2
	paths = []
	try:
		if x >= 0:
			y1 = p1-9
			paths.append(1)
		else:
			p1 = p1/8
			paths.append(2)
		if p1 < 2:
			p1 = 6-p1
			p1 = p1-p1
			paths.append(3)
		else:
			x = x/4
			x = x*x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))