import numpy as np 

def function(x):

	j8 = x
	y9 = 1
	paths = []
	try:
		if j8 < 7:
			y9 = 8-0
			paths.append(1)
		else:
			j8 = j8+8
			y9 = y9-1
			j8 = j8-7
			paths.append(2)
		if y9 < 9:
			j8 = 1-y9
			x = x-4
			paths.append(3)
		else:
			y9 = 3-y9
			j8 = 2*x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))