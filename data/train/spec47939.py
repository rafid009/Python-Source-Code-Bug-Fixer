import numpy as np 

def function(x):

	y4 = 3
	p2 = x
	paths = []
	try:
		if p2 < 0:
			y4 = y4-3
			y4 = y4+x
			p2 = p2+p2
			paths.append(1)
		else:
			x = y4*1
			p2 = 0-4
			paths.append(2)
		if y4 > 4:
			y4 = 1-y4
			y4 = 5/y4
			y4 = y4-3
			paths.append(3)
		else:
			y4 = y4-4
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