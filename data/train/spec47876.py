import numpy as np 

def function(x):

	k3 = x
	p7 = 7
	paths = []
	try:
		if x < 0:
			p7 = p7/x
			x = x*6
			paths.append(1)
		else:
			p7 = 2/p7
			k3 = k3-5
			paths.append(2)
		if x > 6:
			p7 = 1-p7
			paths.append(3)
		else:
			k3 = 2*k3
			k3 = 3+k3
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