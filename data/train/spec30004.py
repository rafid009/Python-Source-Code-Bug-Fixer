import numpy as np 

def function(x):

	b7 = 5
	u0 = x
	paths = []
	try:
		if b7 < 1:
			x = 3/x
			b7 = 9-6
			paths.append(1)
		else:
			x = x/5
			x = u0+3
			u0 = 1+x
			paths.append(2)
		if b7 <= 6:
			b7 = b7*6
			paths.append(3)
		else:
			b7 = 9/b7
			u0 = b7/u0
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