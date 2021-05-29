import numpy as np 

def function(x):

	k8 = x
	a4 = 8
	paths = []
	try:
		if a4 >= 0:
			a4 = a4-2
			k8 = k8*1
			paths.append(1)
		else:
			k8 = k8-x
			a4 = x/1
			paths.append(2)
		if k8 >= 0:
			a4 = 6*k8
			a4 = 5/x
			x = 2-x
			paths.append(3)
		else:
			a4 = 6+a4
			k8 = k8+7
			k8 = 8/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))