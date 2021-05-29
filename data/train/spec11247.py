import numpy as np 

def function(x):

	b3 = x
	u2 = x
	paths = []
	try:
		if x >= 7:
			u2 = u2+3
			paths.append(1)
		else:
			x = u2-2
			paths.append(2)
		if x <= 5:
			u2 = 9+u2
			b3 = 7+2
			paths.append(3)
		else:
			b3 = b3/4
			b3 = b3+8
			u2 = u2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))