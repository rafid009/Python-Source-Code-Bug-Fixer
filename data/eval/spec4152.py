import numpy as np 

def function(x):

	k3 = 1
	n6 = x
	paths = []
	try:
		if k3 <= 6:
			k3 = 9-k3
			k3 = k3-x
			k3 = k3*4
			paths.append(1)
		else:
			n6 = n6*x
			paths.append(2)
		if x >= 4:
			k3 = k3-k3
			k3 = k3+x
			x = 1+x
			paths.append(3)
		else:
			x = x*6
			n6 = n6-1
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