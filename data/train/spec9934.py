import numpy as np 

def function(x):

	x4 = 4
	p8 = 6
	paths = []
	try:
		if x4 <= 1:
			x4 = 7-x4
			x = x*x4
			paths.append(1)
		else:
			p8 = p8-5
			paths.append(2)
		if x4 >= 0:
			x4 = 2*x4
			p8 = x*x4
			paths.append(3)
		else:
			x = p8+1
			p8 = p8-x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))