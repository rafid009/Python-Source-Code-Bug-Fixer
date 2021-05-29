import numpy as np 

def function(x):

	u3 = 9
	k0 = 7
	paths = []
	try:
		if u3 < 9:
			u3 = x*k0
			k0 = k0*4
			paths.append(1)
		else:
			u3 = 1/u3
			u3 = 4*u3
			x = 2-x
			paths.append(2)
		if u3 <= 9:
			u3 = 9*6
			paths.append(3)
		else:
			k0 = k0-1
			u3 = x*1
			k0 = k0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))