import numpy as np 

def function(x):

	u2 = x
	k0 = 2
	paths = []
	try:
		if u2 >= 9:
			k0 = k0-1
			u2 = 0/k0
			x = x*4
			paths.append(1)
		else:
			u2 = 3-u2
			paths.append(2)
		if x <= 5:
			x = 2+x
			k0 = 3/k0
			paths.append(3)
		else:
			u2 = u2-2
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