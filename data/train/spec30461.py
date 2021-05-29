import numpy as np 

def function(x):

	p2 = 7
	q8 = 4
	paths = []
	try:
		if x <= 0:
			q8 = q8/5
			paths.append(1)
		else:
			q8 = 9/q8
			q8 = 3*q8
			p2 = 6+p2
			paths.append(2)
		if x >= 8:
			q8 = 8*2
			q8 = 3/q8
			paths.append(3)
		else:
			q8 = q8-p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))