import numpy as np 

def function(x):

	k0 = 9
	e0 = 2
	paths = []
	try:
		if x <= 7:
			k0 = k0*5
			e0 = 6*2
			paths.append(1)
		else:
			e0 = e0*e0
			x = x*2
			x = 6+x
			paths.append(2)
		if k0 <= 7:
			k0 = 9+x
			e0 = 2/e0
			paths.append(3)
		else:
			k0 = k0/x
			x = e0-x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		e0 = k0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))