import numpy as np 

def function(x):

	k8 = 5
	n2 = x
	x = 1
	paths = []
	try:
		if n2 < 9:
			k8 = k8+8
			paths.append(1)
		else:
			k8 = 2/k8
			k8 = 4-x
			n2 = 5-x
			paths.append(2)
		if k8 < 2:
			n2 = x+k8
			n2 = 9/n2
			k8 = k8/7
			paths.append(3)
		else:
			x = x+x
			k8 = k8-7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		k8 = n2**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))