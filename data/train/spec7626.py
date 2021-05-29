import numpy as np 

def function(x):

	y9 = 7
	p3 = x
	paths = []
	try:
		if y9 <= 6:
			x = x*p3
			p3 = x/4
			paths.append(1)
		else:
			p3 = p3*7
			y9 = y9*2
			paths.append(2)
		if x <= 5:
			y9 = y9-p3
			paths.append(3)
		else:
			y9 = y9/7
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