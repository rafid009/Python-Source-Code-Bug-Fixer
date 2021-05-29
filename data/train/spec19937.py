import numpy as np 

def function(x):

	o8 = 8
	k8 = x
	x = 0
	paths = []
	try:
		if k8 > 6:
			k8 = 6/k8
			paths.append(1)
		else:
			x = 0-8
			paths.append(2)
		if o8 < 9:
			o8 = 4+k8
			paths.append(3)
		else:
			o8 = o8-k8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		k8 = o8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))