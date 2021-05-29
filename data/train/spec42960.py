import numpy as np 

def function(x):

	o1 = 0
	y9 = 7
	paths = []
	try:
		if o1 <= 5:
			o1 = o1+9
			x = x*8
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if x <= 8:
			o1 = 6+o1
			x = x*1
			paths.append(3)
		else:
			o1 = x/y9
			x = 9-x
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))