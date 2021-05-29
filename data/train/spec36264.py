import numpy as np 

def function(x):

	k8 = 8
	r9 = 1
	x = x
	paths = []
	try:
		if k8 <= 5:
			r9 = r9-4
			r9 = 5/r9
			paths.append(1)
		else:
			k8 = 7-k8
			r9 = r9-8
			x = 3/x
			paths.append(2)
		if r9 < 1:
			x = r9/x
			paths.append(3)
		else:
			x = r9+x
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