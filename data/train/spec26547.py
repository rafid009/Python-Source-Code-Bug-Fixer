import numpy as np 

def function(x):

	a9 = 6
	k8 = x
	x = x
	paths = []
	try:
		if a9 <= 9:
			x = 9+a9
			k8 = 3/k8
			paths.append(1)
		else:
			a9 = a9-5
			k8 = 3+k8
			a9 = a9-3
			paths.append(2)
		if k8 >= 1:
			x = k8-x
			x = k8+x
			paths.append(3)
		else:
			x = x-9
			x = 7*x
			x = x*a9
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		a9 = k8**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))