import numpy as np 

def function(x):

	o4 = x
	k8 = 2
	paths = []
	try:
		if x > 7:
			x = 0/x
			paths.append(1)
		else:
			x = x/x
			x = o4+x
			paths.append(2)
		if o4 > 1:
			o4 = o4*o4
			paths.append(3)
		else:
			o4 = 7/1
			k8 = 7*k8
			k8 = k8-9
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