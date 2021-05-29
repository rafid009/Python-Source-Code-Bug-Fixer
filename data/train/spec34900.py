import numpy as np 

def function(x):

	w0 = x
	k8 = 3
	paths = []
	try:
		if x <= 3:
			k8 = 1-8
			x = k8+x
			k8 = k8+1
			paths.append(1)
		else:
			k8 = k8/3
			paths.append(2)
		if x < 1:
			k8 = k8-w0
			paths.append(3)
		else:
			k8 = k8+5
			k8 = x-w0
			k8 = 5-2
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))