import numpy as np 

def function(x):

	k8 = 9
	d2 = 0
	x = x
	paths = []
	try:
		if d2 > 5:
			x = 3/x
			paths.append(1)
		else:
			x = x-5
			x = x+d2
			paths.append(2)
		if k8 <= 3:
			k8 = 6+0
			k8 = k8/5
			paths.append(3)
		else:
			k8 = d2*7
			k8 = k8/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))