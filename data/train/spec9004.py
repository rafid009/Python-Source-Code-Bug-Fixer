import numpy as np 

def function(x):

	k8 = 8
	d9 = x
	paths = []
	try:
		if d9 <= 2:
			k8 = 8-k8
			k8 = k8+3
			paths.append(1)
		else:
			x = k8*9
			k8 = d9*4
			paths.append(2)
		if d9 <= 9:
			k8 = k8*4
			d9 = d9+3
			paths.append(3)
		else:
			x = k8+x
			k8 = k8*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))