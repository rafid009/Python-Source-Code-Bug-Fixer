import numpy as np 

def function(x):

	y9 = 5
	q9 = x
	paths = []
	try:
		if y9 > 6:
			q9 = y9+q9
			paths.append(1)
		else:
			x = 2*9
			y9 = 7+y9
			paths.append(2)
		if y9 >= 7:
			q9 = q9-x
			paths.append(3)
		else:
			q9 = y9+y9
			x = 0*1
			q9 = 8*4
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))