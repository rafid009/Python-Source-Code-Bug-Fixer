import numpy as np 

def function(x):

	y9 = x
	b4 = x
	paths = []
	try:
		if x >= 3:
			b4 = 5+x
			y9 = x*5
			y9 = 1-y9
			paths.append(1)
		else:
			x = 6/x
			x = x/9
			paths.append(2)
		if y9 > 4:
			x = x+x
			paths.append(3)
		else:
			b4 = b4/x
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