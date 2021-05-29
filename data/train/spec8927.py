import numpy as np 

def function(x):

	y5 = x
	k8 = x
	paths = []
	try:
		if x <= 2:
			x = x-6
			y5 = y5*6
			x = 8+x
			paths.append(1)
		else:
			x = 8-4
			k8 = k8*k8
			k8 = 8-k8
			paths.append(2)
		if y5 > 1:
			k8 = y5/k8
			x = x-6
			paths.append(3)
		else:
			y5 = k8-2
			k8 = k8+6
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))