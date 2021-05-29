import numpy as np 

def function(x):

	y0 = x
	k8 = 8
	paths = []
	try:
		if k8 < 5:
			y0 = y0*1
			k8 = 5*k8
			y0 = 6/y0
			paths.append(1)
		else:
			y0 = 1+y0
			paths.append(2)
		if x <= 1:
			k8 = 1+y0
			paths.append(3)
		else:
			x = x/5
			y0 = 6*y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))