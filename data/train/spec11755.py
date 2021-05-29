import numpy as np 

def function(x):

	y9 = x
	q2 = 2
	paths = []
	try:
		if q2 <= 5:
			y9 = 9-y9
			paths.append(1)
		else:
			y9 = y9-4
			x = y9*4
			paths.append(2)
		if y9 <= 8:
			x = 4-q2
			q2 = q2/8
			y9 = x+q2
			paths.append(3)
		else:
			y9 = 3-9
			x = 8/x
			q2 = 7+1
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