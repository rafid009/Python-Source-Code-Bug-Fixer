import numpy as np 

def function(x):

	w6 = x
	y9 = x
	x = x
	paths = []
	try:
		if y9 >= 7:
			y9 = w6*w6
			paths.append(1)
		else:
			y9 = y9-2
			paths.append(2)
		if w6 <= 4:
			x = x+5
			paths.append(3)
		else:
			x = 1+x
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