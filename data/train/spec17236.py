import numpy as np 

def function(x):

	y9 = x
	o2 = 2
	paths = []
	try:
		if y9 > 7:
			y9 = 6-x
			x = 7*x
			o2 = 5/o2
			paths.append(1)
		else:
			o2 = 6+o2
			paths.append(2)
		if x <= 8:
			x = x-o2
			x = x*4
			paths.append(3)
		else:
			x = 4-8
			y9 = 6-y9
			x = x-6
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