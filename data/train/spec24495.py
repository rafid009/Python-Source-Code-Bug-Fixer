import numpy as np 

def function(x):

	y5 = x
	k8 = 8
	paths = []
	try:
		if x > 6:
			x = x/x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x >= 6:
			k8 = 9/k8
			k8 = y5-6
			paths.append(3)
		else:
			k8 = k8-y5
			x = k8+k8
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		y5 = k8**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))