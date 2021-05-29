import numpy as np 

def function(x):

	p4 = x
	z8 = x
	paths = []
	try:
		if z8 >= 2:
			p4 = p4*z8
			paths.append(1)
		else:
			p4 = p4/z8
			paths.append(2)
		if p4 > 1:
			x = x+p4
			paths.append(3)
		else:
			p4 = 1/p4
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))