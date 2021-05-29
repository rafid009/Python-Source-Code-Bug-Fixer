import numpy as np 

def function(x):

	k0 = 7
	k3 = 0
	paths = []
	try:
		if k3 < 1:
			x = 4+x
			k0 = k0*4
			paths.append(1)
		else:
			k3 = 1/2
			k0 = k0/8
			k3 = x+k3
			paths.append(2)
		if k3 >= 8:
			k3 = k0-k3
			k3 = k3*7
			paths.append(3)
		else:
			k0 = k0/5
			k3 = x+9
			k3 = 5*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))