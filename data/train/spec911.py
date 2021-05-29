import numpy as np 

def function(x):

	k3 = 1
	k4 = 2
	paths = []
	try:
		if x > 4:
			k3 = k3-2
			k3 = k3-k3
			paths.append(1)
		else:
			x = k4+x
			paths.append(2)
		if k3 >= 3:
			k3 = 1/k4
			k3 = k3/9
			paths.append(3)
		else:
			k3 = 6/9
			k3 = k3*4
			k3 = k4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))