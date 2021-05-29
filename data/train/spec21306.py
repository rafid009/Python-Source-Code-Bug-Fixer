import numpy as np 

def function(x):

	k8 = x
	n0 = 5
	paths = []
	try:
		if k8 >= 6:
			k8 = x+k8
			paths.append(1)
		else:
			x = n0*5
			paths.append(2)
		if n0 <= 7:
			n0 = n0*6
			x = x+n0
			x = x-9
			paths.append(3)
		else:
			k8 = k8+0
			n0 = x-n0
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