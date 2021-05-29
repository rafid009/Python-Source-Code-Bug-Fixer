import numpy as np 

def function(x):

	x7 = x
	p1 = 9
	paths = []
	try:
		if x7 > 2:
			x7 = 2*p1
			p1 = 4*p1
			p1 = 3*p1
			paths.append(1)
		else:
			x7 = x7/p1
			p1 = p1/p1
			paths.append(2)
		if x7 > 7:
			p1 = p1*6
			paths.append(3)
		else:
			x7 = 7*x7
			p1 = x7-0
			x = x-p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))