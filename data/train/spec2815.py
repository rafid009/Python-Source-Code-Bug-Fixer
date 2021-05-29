import numpy as np 

def function(x):

	k8 = x
	w5 = 1
	paths = []
	try:
		if w5 < 8:
			w5 = 0-w5
			w5 = k8-3
			k8 = 3*k8
			paths.append(1)
		else:
			k8 = k8-9
			x = x*8
			w5 = w5*4
			paths.append(2)
		if x >= 4:
			k8 = 1/k8
			k8 = 9/k8
			paths.append(3)
		else:
			w5 = w5/3
			k8 = k8/5
			k8 = w5*x
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