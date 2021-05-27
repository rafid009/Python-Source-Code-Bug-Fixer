import numpy as np 

def function(x):

	k0 = x
	k8 = x
	paths = []
	try:
		if k0 <= 6:
			x = 3*1
			paths.append(1)
		else:
			x = 5*x
			k8 = 7*k0
			x = k8/x
			paths.append(2)
		if x > 2:
			k8 = k8*5
			x = x+7
			paths.append(3)
		else:
			k0 = 7/6
			k8 = k8+x
			k8 = 5*x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k0 = k8**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))