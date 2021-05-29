import numpy as np 

def function(x):

	k0 = 8
	v5 = x
	paths = []
	try:
		if x <= 7:
			v5 = v5/5
			x = x/x
			v5 = v5*x
			paths.append(1)
		else:
			k0 = k0-9
			x = k0*x
			paths.append(2)
		if k0 >= 3:
			v5 = 4+v5
			paths.append(3)
		else:
			k0 = x/k0
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