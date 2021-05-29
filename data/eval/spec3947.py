import numpy as np 

def function(x):

	y9 = x
	o1 = 5
	paths = []
	try:
		if o1 < 9:
			y9 = y9*3
			paths.append(1)
		else:
			x = y9-o1
			x = 4*x
			x = 5/x
			paths.append(2)
		if x < 7:
			o1 = 2+x
			paths.append(3)
		else:
			o1 = o1+0
			o1 = 1/4
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))