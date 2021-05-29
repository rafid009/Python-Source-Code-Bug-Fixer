import numpy as np 

def function(x):

	k0 = 1
	a2 = x
	paths = []
	try:
		if a2 < 6:
			k0 = a2/3
			k0 = k0/k0
			k0 = 6/k0
			paths.append(1)
		else:
			k0 = k0*k0
			k0 = a2-6
			a2 = 1-7
			paths.append(2)
		if k0 >= 4:
			k0 = x+k0
			k0 = k0-k0
			paths.append(3)
		else:
			x = a2*x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))