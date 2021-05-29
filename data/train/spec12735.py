import numpy as np 

def function(x):

	u0 = x
	b8 = x
	paths = []
	try:
		if x < 6:
			u0 = b8/b8
			paths.append(1)
		else:
			x = x/1
			x = x-3
			b8 = 0*b8
			paths.append(2)
		if x > 4:
			b8 = b8-8
			u0 = u0*7
			paths.append(3)
		else:
			b8 = b8-8
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		u0 = b8**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))