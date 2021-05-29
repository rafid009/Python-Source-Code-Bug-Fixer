import numpy as np 

def function(x):

	k0 = x
	g5 = x
	x = 2
	paths = []
	try:
		if g5 < 0:
			x = 8/k0
			x = 1+x
			paths.append(1)
		else:
			x = 8/4
			k0 = g5-8
			paths.append(2)
		if k0 >= 7:
			k0 = k0*k0
			x = x*6
			x = x+x
			paths.append(3)
		else:
			k0 = k0+2
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))