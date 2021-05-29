import numpy as np 

def function(x):

	k8 = x
	h8 = 5
	x = 7
	paths = []
	try:
		if x > 7:
			k8 = 9/k8
			paths.append(1)
		else:
			k8 = 6/k8
			x = x/x
			k8 = k8-9
			paths.append(2)
		if x < 3:
			k8 = k8*5
			paths.append(3)
		else:
			k8 = h8/1
			h8 = h8*6
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