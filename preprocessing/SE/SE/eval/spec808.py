import numpy as np 

def function(x):

	k8 = 6
	a0 = x
	paths = []
	try:
		if x <= 4:
			k8 = x+x
			k8 = 4+a0
			paths.append(1)
		else:
			k8 = a0/x
			paths.append(2)
		if x >= 8:
			k8 = k8-7
			k8 = k8*x
			k8 = k8+5
			paths.append(3)
		else:
			a0 = x-0
			k8 = k8*5
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))