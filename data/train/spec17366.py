import numpy as np 

def function(x):

	y9 = x
	q2 = x
	paths = []
	try:
		if x <= 1:
			y9 = 2*q2
			paths.append(1)
		else:
			x = x/1
			x = q2/7
			y9 = x-2
			paths.append(2)
		if y9 <= 2:
			q2 = q2*5
			paths.append(3)
		else:
			x = 8/q2
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		q2 = y9**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))