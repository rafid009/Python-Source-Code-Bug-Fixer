import numpy as np 

def function(x):

	k8 = 4
	v9 = 5
	paths = []
	try:
		if v9 < 0:
			k8 = v9*8
			paths.append(1)
		else:
			v9 = v9/k8
			v9 = v9/9
			k8 = v9-2
			paths.append(2)
		if x <= 3:
			k8 = 8/8
			x = x-5
			paths.append(3)
		else:
			v9 = v9/k8
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