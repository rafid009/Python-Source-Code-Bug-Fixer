import numpy as np 

def function(x):

	y9 = x
	a5 = x
	x = 2
	paths = []
	try:
		if y9 > 0:
			x = a5/x
			y9 = x*0
			paths.append(1)
		else:
			a5 = x/4
			a5 = y9-0
			x = x-y9
			paths.append(2)
		if y9 < 8:
			x = 0-x
			paths.append(3)
		else:
			x = 6+x
			y9 = a5*y9
			a5 = x-0
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))