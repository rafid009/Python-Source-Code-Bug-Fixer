import numpy as np 

def function(x):

	l0 = x
	p1 = x
	paths = []
	try:
		if p1 > 9:
			x = x*6
			paths.append(1)
		else:
			l0 = l0/7
			paths.append(2)
		if p1 > 9:
			p1 = 2*p1
			paths.append(3)
		else:
			p1 = p1/1
			x = x-9
			x = x/p1
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