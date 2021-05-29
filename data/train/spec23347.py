import numpy as np 

def function(x):

	x2 = x
	k8 = 2
	paths = []
	try:
		if k8 >= 2:
			x = x2*k8
			x2 = x2+4
			paths.append(1)
		else:
			x = 2-x
			k8 = 5/k8
			paths.append(2)
		if k8 < 9:
			k8 = k8*5
			paths.append(3)
		else:
			k8 = x2-2
			x = x-k8
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