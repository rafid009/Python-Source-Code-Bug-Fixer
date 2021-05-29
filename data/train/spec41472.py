import numpy as np 

def function(x):

	l9 = 8
	y9 = x
	x = x
	paths = []
	try:
		if y9 > 8:
			y9 = 7+y9
			x = 5/x
			x = 8*x
			paths.append(1)
		else:
			l9 = x/x
			paths.append(2)
		if x >= 2:
			l9 = l9+4
			paths.append(3)
		else:
			x = l9*x
			x = x/l9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		l9 = y9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))