import numpy as np 

def function(x):

	k0 = 4
	e0 = x
	paths = []
	try:
		if k0 < 3:
			k0 = 5/k0
			k0 = 0*1
			paths.append(1)
		else:
			e0 = 9+e0
			e0 = 9+e0
			paths.append(2)
		if e0 <= 1:
			e0 = e0*k0
			paths.append(3)
		else:
			e0 = e0*5
			k0 = k0/9
			x = 1+k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))