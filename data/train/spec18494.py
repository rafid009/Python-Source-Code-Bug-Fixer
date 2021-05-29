import numpy as np 

def function(x):

	y9 = x
	n1 = 1
	paths = []
	try:
		if n1 >= 1:
			x = x+3
			x = x-7
			n1 = 4+x
			paths.append(1)
		else:
			y9 = x*y9
			x = x*3
			n1 = 7*n1
			paths.append(2)
		if x >= 0:
			y9 = y9*9
			paths.append(3)
		else:
			n1 = n1+1
			n1 = n1/5
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))