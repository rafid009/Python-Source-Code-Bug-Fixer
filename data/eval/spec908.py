import numpy as np 

def function(x):

	k3 = x
	x4 = x
	paths = []
	try:
		if x4 < 7:
			x4 = x4+6
			k3 = k3+3
			k3 = 3-7
			paths.append(1)
		else:
			k3 = k3*4
			x = 7/2
			x4 = x4*x4
			paths.append(2)
		if k3 > 9:
			x = x*4
			paths.append(3)
		else:
			x4 = k3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))