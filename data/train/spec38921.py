import numpy as np 

def function(x):

	k8 = x
	d9 = 3
	x = 9
	paths = []
	try:
		if k8 < 5:
			k8 = k8-d9
			d9 = d9*7
			paths.append(1)
		else:
			d9 = 3-d9
			k8 = 1/k8
			paths.append(2)
		if x > 5:
			x = x/1
			paths.append(3)
		else:
			k8 = k8*7
			x = 8-x
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