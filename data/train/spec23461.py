import numpy as np 

def function(x):

	n3 = 6
	k8 = x
	paths = []
	try:
		if k8 >= 9:
			k8 = k8-x
			paths.append(1)
		else:
			k8 = 5/4
			n3 = n3-8
			k8 = k8+8
			paths.append(2)
		if k8 >= 3:
			k8 = k8*4
			n3 = n3/2
			x = n3*4
			paths.append(3)
		else:
			x = 4+2
			x = x+x
			k8 = 3*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))