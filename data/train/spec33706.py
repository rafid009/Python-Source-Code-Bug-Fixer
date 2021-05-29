import numpy as np 

def function(x):

	y9 = x
	l2 = x
	paths = []
	try:
		if l2 < 5:
			l2 = l2*3
			paths.append(1)
		else:
			x = 1*l2
			paths.append(2)
		if y9 > 2:
			x = x-1
			l2 = l2/l2
			l2 = l2+y9
			paths.append(3)
		else:
			x = y9+3
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