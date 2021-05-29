import numpy as np 

def function(x):

	p7 = x
	k8 = 3
	paths = []
	try:
		if x >= 3:
			k8 = 4-1
			paths.append(1)
		else:
			k8 = 6*7
			paths.append(2)
		if k8 > 0:
			k8 = x+3
			paths.append(3)
		else:
			k8 = p7-k8
			p7 = 9-p7
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