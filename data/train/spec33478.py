import numpy as np 

def function(x):

	x7 = 5
	k8 = 1
	paths = []
	try:
		if x <= 4:
			x7 = 7*x
			paths.append(1)
		else:
			k8 = 8/k8
			k8 = 8-k8
			paths.append(2)
		if x >= 9:
			k8 = k8*0
			x7 = x7*x7
			paths.append(3)
		else:
			k8 = 3-9
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