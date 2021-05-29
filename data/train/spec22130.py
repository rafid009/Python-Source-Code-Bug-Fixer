import numpy as np 

def function(x):

	l2 = 2
	k8 = 6
	paths = []
	try:
		if k8 >= 4:
			l2 = 1/k8
			paths.append(1)
		else:
			k8 = 1/k8
			k8 = k8+6
			paths.append(2)
		if k8 >= 1:
			l2 = l2-5
			k8 = k8*9
			paths.append(3)
		else:
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		k8 = l2**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))