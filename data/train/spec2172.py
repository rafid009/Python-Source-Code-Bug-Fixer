import numpy as np 

def function(x):

	k2 = 5
	r8 = 3
	paths = []
	try:
		if r8 < 6:
			r8 = r8/k2
			paths.append(1)
		else:
			r8 = 3-r8
			r8 = 6-x
			x = x*k2
			paths.append(2)
		if r8 <= 0:
			x = 8-x
			k2 = 1*3
			r8 = 0-2
			paths.append(3)
		else:
			k2 = k2/x
			x = 2/k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))