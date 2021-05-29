import numpy as np 

def function(x):

	k8 = x
	o5 = x
	paths = []
	try:
		if x < 4:
			o5 = o5*x
			paths.append(1)
		else:
			o5 = x+o5
			paths.append(2)
		if x > 3:
			x = 1+x
			k8 = k8+0
			k8 = k8-1
			paths.append(3)
		else:
			k8 = 6-k8
			k8 = 4/k8
			x = 8/x
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