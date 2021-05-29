import numpy as np 

def function(x):

	y9 = x
	o1 = x
	paths = []
	try:
		if x >= 4:
			o1 = o1+1
			paths.append(1)
		else:
			x = 1*x
			o1 = o1+y9
			paths.append(2)
		if x <= 9:
			o1 = o1*3
			o1 = o1-5
			paths.append(3)
		else:
			y9 = o1-y9
			o1 = o1/9
			o1 = 7-7
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