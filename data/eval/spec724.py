import numpy as np 

def function(x):

	u2 = 9
	b0 = x
	paths = []
	try:
		if b0 > 7:
			b0 = 0-8
			paths.append(1)
		else:
			b0 = b0+8
			paths.append(2)
		if b0 < 5:
			u2 = u2*6
			x = 0+x
			paths.append(3)
		else:
			u2 = 3/u2
			u2 = 8/u2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		u2 = b0**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))