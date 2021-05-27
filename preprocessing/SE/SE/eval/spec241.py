import numpy as np 

def function(x):

	k8 = x
	y3 = 5
	paths = []
	try:
		if k8 >= 6:
			k8 = y3+x
			paths.append(1)
		else:
			y3 = y3*3
			k8 = 5*y3
			y3 = k8/y3
			paths.append(2)
		if y3 < 0:
			y3 = y3/4
			y3 = x/y3
			paths.append(3)
		else:
			k8 = 6*k8
			k8 = k8-3
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