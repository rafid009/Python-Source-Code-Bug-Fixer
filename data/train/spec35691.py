import numpy as np 

def function(x):

	z5 = 7
	k8 = x
	paths = []
	try:
		if x > 4:
			z5 = z5+1
			z5 = 2-9
			x = x*0
			paths.append(1)
		else:
			k8 = z5-3
			k8 = 0-k8
			paths.append(2)
		if k8 >= 4:
			k8 = k8-x
			x = 3-x
			paths.append(3)
		else:
			z5 = 6/4
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))