import numpy as np 

def function(x):

	p1 = 3
	y1 = 7
	paths = []
	try:
		if y1 >= 9:
			p1 = p1-p1
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if y1 < 4:
			y1 = x-y1
			x = 7-x
			paths.append(3)
		else:
			x = 4-x
			p1 = 7-x
			p1 = p1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))