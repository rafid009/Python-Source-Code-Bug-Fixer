import numpy as np 

def function(x):

	x4 = x
	u2 = x
	paths = []
	try:
		if x <= 9:
			x = 1-8
			u2 = u2-2
			paths.append(1)
		else:
			x4 = 2/u2
			paths.append(2)
		if u2 < 5:
			x = x/4
			x4 = x4/u2
			u2 = 4-u2
			paths.append(3)
		else:
			x = x/5
			u2 = u2-8
			x4 = x4+7
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