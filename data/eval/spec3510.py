import numpy as np 

def function(x):

	y9 = x
	r0 = 2
	paths = []
	try:
		if x <= 3:
			x = 9/5
			x = 7*5
			r0 = 2+6
			paths.append(1)
		else:
			x = 2-x
			x = 5-x
			paths.append(2)
		if x > 2:
			x = 1-y9
			r0 = 7+3
			paths.append(3)
		else:
			x = x*r0
			x = 7-x
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