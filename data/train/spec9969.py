import numpy as np 

def function(x):

	k8 = 4
	z1 = 0
	x = x
	paths = []
	try:
		if x >= 7:
			z1 = 8/1
			x = 2+x
			paths.append(1)
		else:
			k8 = k8*1
			paths.append(2)
		if z1 >= 7:
			x = 5+x
			k8 = k8/k8
			paths.append(3)
		else:
			z1 = x/7
			x = 7+9
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))