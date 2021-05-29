import numpy as np 

def function(x):

	e2 = 2
	k0 = x
	paths = []
	try:
		if x >= 9:
			x = x/8
			paths.append(1)
		else:
			e2 = e2+x
			k0 = 8-k0
			paths.append(2)
		if e2 > 9:
			x = 7+x
			k0 = x+k0
			k0 = k0-k0
			paths.append(3)
		else:
			k0 = k0-7
			x = x*k0
			k0 = 0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))