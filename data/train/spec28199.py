import numpy as np 

def function(x):

	p4 = 6
	n0 = 1
	paths = []
	try:
		if x > 0:
			n0 = n0+1
			p4 = 6*p4
			n0 = 5-x
			paths.append(1)
		else:
			p4 = 9-7
			paths.append(2)
		if p4 <= 8:
			p4 = 1-0
			paths.append(3)
		else:
			p4 = p4+6
			p4 = n0/x
			n0 = 8*n0
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