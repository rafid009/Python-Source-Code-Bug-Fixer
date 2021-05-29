import numpy as np 

def function(x):

	y9 = 7
	p3 = 5
	paths = []
	try:
		if x > 2:
			p3 = x*p3
			paths.append(1)
		else:
			y9 = x*y9
			p3 = y9-x
			p3 = 3-5
			paths.append(2)
		if y9 >= 5:
			x = 6-x
			x = x/y9
			paths.append(3)
		else:
			x = x*2
			p3 = p3-3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		y9 = p3**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))