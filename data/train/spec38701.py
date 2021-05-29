import numpy as np 

def function(x):

	n0 = 8
	p7 = 1
	paths = []
	try:
		if n0 < 9:
			x = x+n0
			n0 = n0+n0
			paths.append(1)
		else:
			p7 = n0+9
			n0 = n0*6
			x = x*5
			paths.append(2)
		if n0 <= 7:
			n0 = p7/x
			n0 = 9-5
			n0 = x/n0
			paths.append(3)
		else:
			n0 = 9+n0
			x = x/9
			p7 = p7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))