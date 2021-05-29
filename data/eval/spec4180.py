import numpy as np 

def function(x):

	l1 = 7
	p0 = 0
	paths = []
	try:
		if x > 7:
			p0 = 7+p0
			p0 = p0*5
			x = x+6
			paths.append(1)
		else:
			l1 = l1/3
			l1 = l1-9
			l1 = l1+4
			paths.append(2)
		if x < 6:
			x = 9/x
			paths.append(3)
		else:
			l1 = l1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))