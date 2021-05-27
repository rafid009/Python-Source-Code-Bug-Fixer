import numpy as np 

def function(x):

	a7 = x
	k8 = 5
	paths = []
	try:
		if x <= 6:
			x = 2/x
			a7 = 0/3
			paths.append(1)
		else:
			k8 = k8-k8
			paths.append(2)
		if x < 3:
			x = x+4
			k8 = a7-a7
			x = x-2
			paths.append(3)
		else:
			x = 7/x
			a7 = x+a7
			k8 = a7-k8
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		a7 = k8**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))