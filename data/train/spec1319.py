import numpy as np 

def function(x):

	k0 = x
	p1 = 2
	paths = []
	try:
		if p1 > 2:
			k0 = 8-k0
			k0 = p1/6
			paths.append(1)
		else:
			p1 = p1+4
			k0 = 9+2
			paths.append(2)
		if p1 < 1:
			p1 = 3/p1
			p1 = p1+3
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))