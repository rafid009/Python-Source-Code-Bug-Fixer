import numpy as np 

def function(x):

	y9 = 6
	i5 = x
	paths = []
	try:
		if y9 < 4:
			y9 = y9-4
			y9 = 3+y9
			paths.append(1)
		else:
			i5 = i5*9
			y9 = x*8
			y9 = 5*y9
			paths.append(2)
		if i5 >= 3:
			x = 0-y9
			i5 = i5-5
			y9 = 5+9
			paths.append(3)
		else:
			y9 = 0*4
			i5 = i5*7
			y9 = y9*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))