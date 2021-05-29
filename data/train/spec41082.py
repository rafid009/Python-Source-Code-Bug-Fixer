import numpy as np 

def function(x):

	u3 = 2
	y9 = 5
	paths = []
	try:
		if y9 <= 7:
			u3 = u3-u3
			x = 9/x
			x = x*1
			paths.append(1)
		else:
			x = 9*x
			y9 = 9*9
			x = x*x
			paths.append(2)
		if x >= 6:
			u3 = y9/1
			paths.append(3)
		else:
			u3 = u3+u3
			y9 = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))