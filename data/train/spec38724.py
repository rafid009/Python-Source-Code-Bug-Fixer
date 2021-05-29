import numpy as np 

def function(x):

	k0 = 5
	r9 = 0
	paths = []
	try:
		if k0 <= 0:
			x = 5/2
			paths.append(1)
		else:
			x = x/8
			k0 = 4-8
			k0 = k0-7
			paths.append(2)
		if x < 1:
			k0 = r9+1
			r9 = 3/4
			k0 = k0/9
			paths.append(3)
		else:
			r9 = r9+9
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))