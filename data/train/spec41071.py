import numpy as np 

def function(x):

	a0 = x
	u2 = x
	x = 2
	paths = []
	try:
		if x < 5:
			u2 = u2+0
			u2 = u2-2
			a0 = 0+2
			paths.append(1)
		else:
			a0 = a0/5
			paths.append(2)
		if u2 < 5:
			x = 5-9
			u2 = u2/2
			paths.append(3)
		else:
			a0 = a0-4
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