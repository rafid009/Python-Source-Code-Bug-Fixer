import numpy as np 

def function(x):

	a2 = 7
	y9 = 9
	paths = []
	try:
		if x >= 7:
			x = x*1
			a2 = 6+4
			paths.append(1)
		else:
			y9 = 0/1
			y9 = y9-2
			y9 = 0+y9
			paths.append(2)
		if a2 < 0:
			y9 = y9/8
			a2 = 3/7
			paths.append(3)
		else:
			y9 = y9*0
			a2 = 0+a2
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