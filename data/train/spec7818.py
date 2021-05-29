import numpy as np 

def function(x):

	p7 = 7
	y9 = x
	paths = []
	try:
		if x >= 6:
			p7 = x*p7
			y9 = y9-9
			y9 = p7-6
			paths.append(1)
		else:
			x = 6-9
			paths.append(2)
		if p7 > 3:
			y9 = 7/3
			p7 = y9+p7
			p7 = 5+1
			paths.append(3)
		else:
			y9 = 6-x
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