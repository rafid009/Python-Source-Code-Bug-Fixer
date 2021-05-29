import numpy as np 

def function(x):

	i0 = 0
	k8 = x
	paths = []
	try:
		if x > 0:
			x = x-6
			i0 = 6+i0
			k8 = 4+7
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if k8 > 9:
			k8 = k8-8
			paths.append(3)
		else:
			x = k8+5
			k8 = 3/k8
			i0 = k8+i0
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))