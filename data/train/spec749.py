import numpy as np 

def function(x):

	k2 = x
	k8 = 4
	paths = []
	try:
		if k8 >= 9:
			x = x+3
			paths.append(1)
		else:
			k2 = k2/x
			k8 = 3*6
			k8 = 4*k8
			paths.append(2)
		if k8 < 0:
			k8 = k2*3
			x = x*k8
			k2 = 7/8
			paths.append(3)
		else:
			x = 2+x
			k8 = 5/x
			k2 = 7*k2
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