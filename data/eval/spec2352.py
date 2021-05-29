import numpy as np 

def function(x):

	y9 = 4
	l1 = 4
	paths = []
	try:
		if l1 >= 6:
			x = x/l1
			paths.append(1)
		else:
			y9 = y9/9
			paths.append(2)
		if l1 < 4:
			y9 = y9+1
			paths.append(3)
		else:
			l1 = l1-x
			y9 = y9+1
			l1 = l1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))