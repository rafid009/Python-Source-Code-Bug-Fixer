import numpy as np 

def function(x):

	b5 = 7
	u0 = x
	paths = []
	try:
		if x < 0:
			u0 = x/u0
			b5 = 9+u0
			paths.append(1)
		else:
			b5 = b5*b5
			x = 1*3
			u0 = 1*5
			paths.append(2)
		if b5 <= 4:
			x = x-5
			u0 = 7-u0
			paths.append(3)
		else:
			b5 = b5-9
			u0 = u0*9
			b5 = 0-b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))