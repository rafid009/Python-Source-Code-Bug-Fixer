import numpy as np 

def function(x):

	y9 = 5
	j4 = 4
	paths = []
	try:
		if j4 >= 6:
			y9 = j4+x
			x = 9-x
			x = y9-x
			paths.append(1)
		else:
			j4 = x*0
			paths.append(2)
		if j4 <= 7:
			y9 = y9/y9
			y9 = 7-0
			paths.append(3)
		else:
			j4 = j4*y9
			y9 = y9-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))