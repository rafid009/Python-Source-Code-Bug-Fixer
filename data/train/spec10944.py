import numpy as np 

def function(x):

	y9 = x
	p3 = 2
	paths = []
	try:
		if y9 < 3:
			y9 = 4/y9
			paths.append(1)
		else:
			x = 9+p3
			paths.append(2)
		if p3 < 4:
			y9 = y9+x
			x = x*4
			paths.append(3)
		else:
			x = x+y9
			p3 = y9-8
			p3 = 6+p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))