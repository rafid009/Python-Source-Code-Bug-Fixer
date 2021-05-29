import numpy as np 

def function(x):

	y9 = x
	w7 = x
	x = 9
	paths = []
	try:
		if x <= 7:
			x = 8-x
			w7 = w7*w7
			x = w7/y9
			paths.append(1)
		else:
			y9 = w7*w7
			paths.append(2)
		if w7 <= 9:
			w7 = w7+y9
			paths.append(3)
		else:
			w7 = x-w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		y9 = w7**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))