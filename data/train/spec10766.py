import numpy as np 

def function(x):

	w9 = x
	k8 = 2
	paths = []
	try:
		if x > 6:
			w9 = 2*3
			paths.append(1)
		else:
			x = x+3
			k8 = x*2
			k8 = k8*x
			paths.append(2)
		if k8 >= 3:
			x = 4-k8
			k8 = w9/5
			paths.append(3)
		else:
			k8 = w9-2
			w9 = x+8
			x = w9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))