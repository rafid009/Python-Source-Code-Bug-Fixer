import numpy as np 

def function(x):

	q1 = 8
	y9 = x
	paths = []
	try:
		if y9 < 1:
			q1 = q1/x
			paths.append(1)
		else:
			q1 = q1-9
			y9 = y9/3
			paths.append(2)
		if x > 9:
			q1 = 4+y9
			y9 = y9/q1
			paths.append(3)
		else:
			x = 6*2
			y9 = y9*7
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		y9 = q1**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))