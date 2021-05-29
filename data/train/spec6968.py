import numpy as np 

def function(x):

	q4 = 5
	p8 = x
	paths = []
	try:
		if p8 <= 0:
			p8 = 3*p8
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if p8 < 8:
			x = 4*x
			paths.append(3)
		else:
			p8 = p8-8
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