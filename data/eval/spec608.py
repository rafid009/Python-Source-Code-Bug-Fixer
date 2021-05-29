import numpy as np 

def function(x):

	n3 = 4
	k8 = x
	paths = []
	try:
		if k8 >= 0:
			x = x+7
			x = 4/x
			paths.append(1)
		else:
			x = 1/x
			x = n3/k8
			paths.append(2)
		if n3 > 8:
			x = x*5
			paths.append(3)
		else:
			x = n3+x
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