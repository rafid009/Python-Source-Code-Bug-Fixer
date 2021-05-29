import numpy as np 

def function(x):

	p8 = 9
	v5 = 6
	paths = []
	try:
		if p8 < 1:
			p8 = 2/x
			p8 = p8/6
			p8 = p8/p8
			paths.append(1)
		else:
			p8 = 9*4
			p8 = p8+6
			paths.append(2)
		if x >= 9:
			p8 = p8/7
			paths.append(3)
		else:
			x = x+0
			p8 = v5-p8
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