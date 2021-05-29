import numpy as np 

def function(x):

	k2 = x
	k3 = 5
	paths = []
	try:
		if x <= 0:
			x = 7*7
			k2 = k2*1
			paths.append(1)
		else:
			k2 = 6*5
			paths.append(2)
		if k2 <= 0:
			k3 = k3/k3
			x = 9*k2
			paths.append(3)
		else:
			k2 = k2-6
			k3 = k3-6
			k3 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))