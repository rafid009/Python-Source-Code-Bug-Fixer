import numpy as np 

def function(x):

	r0 = 6
	k8 = x
	paths = []
	try:
		if x <= 6:
			k8 = x/3
			x = k8-x
			paths.append(1)
		else:
			k8 = k8-k8
			paths.append(2)
		if k8 >= 3:
			x = x/1
			paths.append(3)
		else:
			r0 = 0+3
			x = 7-1
			k8 = k8*1
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