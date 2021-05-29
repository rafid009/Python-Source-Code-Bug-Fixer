import numpy as np 

def function(x):

	d8 = 5
	k8 = x
	paths = []
	try:
		if k8 <= 5:
			x = x/3
			paths.append(1)
		else:
			k8 = k8-0
			paths.append(2)
		if d8 <= 6:
			k8 = 0*k8
			k8 = d8-d8
			d8 = 3-d8
			paths.append(3)
		else:
			k8 = 2/k8
			x = 8/5
			x = x*3
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))