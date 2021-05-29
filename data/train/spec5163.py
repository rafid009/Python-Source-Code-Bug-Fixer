import numpy as np 

def function(x):

	k8 = 4
	h2 = x
	x = 2
	paths = []
	try:
		if k8 > 0:
			k8 = k8+5
			x = x-h2
			paths.append(1)
		else:
			k8 = 5+7
			paths.append(2)
		if k8 <= 3:
			k8 = k8/k8
			h2 = h2*0
			k8 = 5+k8
			paths.append(3)
		else:
			k8 = k8+5
			h2 = 7-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))