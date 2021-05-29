import numpy as np 

def function(x):

	y9 = x
	q3 = 7
	paths = []
	try:
		if q3 >= 3:
			x = x/x
			y9 = y9+9
			paths.append(1)
		else:
			q3 = q3+8
			x = x*7
			x = 1/7
			paths.append(2)
		if y9 <= 4:
			x = 5*8
			x = 5+x
			x = 0/y9
			paths.append(3)
		else:
			q3 = 8/q3
			x = 8+8
			y9 = 3/q3
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		q3 = y9**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))