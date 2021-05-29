import numpy as np 

def function(x):

	k8 = 6
	r2 = 3
	paths = []
	try:
		if k8 > 1:
			r2 = r2/x
			paths.append(1)
		else:
			r2 = x+2
			paths.append(2)
		if x >= 7:
			k8 = k8*5
			k8 = x+x
			paths.append(3)
		else:
			k8 = 1/k8
			k8 = 3-k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))