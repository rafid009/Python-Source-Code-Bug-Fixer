import numpy as np 

def function(x):

	y9 = x
	l4 = 7
	paths = []
	try:
		if y9 < 5:
			l4 = 4/6
			paths.append(1)
		else:
			l4 = l4*3
			x = x-6
			paths.append(2)
		if l4 < 5:
			l4 = l4+5
			y9 = 8-x
			y9 = x-y9
			paths.append(3)
		else:
			x = 4*5
			x = x+6
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		l4 = y9**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))