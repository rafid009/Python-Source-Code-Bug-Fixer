import numpy as np 

def function(x):

	y9 = 8
	o7 = x
	x = x
	paths = []
	try:
		if x > 8:
			x = x+y9
			paths.append(1)
		else:
			o7 = o7*1
			o7 = o7+o7
			o7 = 8+o7
			paths.append(2)
		if x < 5:
			y9 = 8+y9
			paths.append(3)
		else:
			y9 = 2-x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))