import numpy as np 

def function(x):

	r8 = 5
	u2 = x
	paths = []
	try:
		if x >= 6:
			x = 7*6
			paths.append(1)
		else:
			r8 = r8+r8
			paths.append(2)
		if x < 9:
			u2 = 5/u2
			r8 = 9/2
			u2 = u2-r8
			paths.append(3)
		else:
			x = x-x
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