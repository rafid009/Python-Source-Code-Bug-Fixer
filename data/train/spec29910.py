import numpy as np 

def function(x):

	k8 = 3
	o7 = x
	paths = []
	try:
		if x < 6:
			o7 = o7/8
			x = x-7
			paths.append(1)
		else:
			o7 = 3-o7
			x = 2+o7
			o7 = o7/3
			paths.append(2)
		if k8 < 8:
			o7 = k8-o7
			k8 = o7-k8
			paths.append(3)
		else:
			x = o7/x
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