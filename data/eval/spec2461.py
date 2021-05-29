import numpy as np 

def function(x):

	p4 = 6
	x7 = x
	paths = []
	try:
		if p4 > 6:
			x = 3/x
			paths.append(1)
		else:
			p4 = p4+2
			p4 = p4/x7
			p4 = 5+p4
			paths.append(2)
		if p4 < 8:
			x7 = 3/x7
			paths.append(3)
		else:
			p4 = 8*p4
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