import numpy as np 

def function(x):

	k1 = 6
	k8 = 1
	x = 7
	paths = []
	try:
		if k8 <= 0:
			k8 = k8+5
			k8 = k8-7
			paths.append(1)
		else:
			k1 = k1*3
			x = k1-x
			paths.append(2)
		if k8 > 8:
			k1 = k8-2
			k1 = k1*0
			paths.append(3)
		else:
			x = 3-8
			k8 = k8+5
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