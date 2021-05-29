import numpy as np 

def function(x):

	u0 = x
	k8 = 7
	paths = []
	try:
		if x > 5:
			k8 = k8/k8
			paths.append(1)
		else:
			k8 = 8-k8
			u0 = u0+6
			paths.append(2)
		if x < 7:
			x = x-6
			paths.append(3)
		else:
			x = x-5
			u0 = 2-u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))