import numpy as np 

def function(x):

	k8 = x
	paths = []
	try:
		if k8 >= 2:
			k8 = x/5
			k8 = 9-k8
			k8 = 8/k8
			paths.append(1)
		else:
			k8 = k8*2
			paths.append(2)
		if k8 <= 8:
			x = x*5
			x = x/8
			x = k8*3
			paths.append(3)
		else:
			x = 0-x
			k8 = k8+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))