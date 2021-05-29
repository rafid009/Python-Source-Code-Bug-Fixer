import numpy as np 

def function(x):

	h5 = x
	k8 = x
	paths = []
	try:
		if k8 > 4:
			k8 = 2-k8
			k8 = 2*h5
			paths.append(1)
		else:
			k8 = k8/7
			x = x-7
			k8 = 4*k8
			paths.append(2)
		if k8 >= 5:
			h5 = 9-h5
			k8 = k8+9
			x = 2*x
			paths.append(3)
		else:
			x = h5+2
			k8 = h5/4
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		h5 = k8**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))