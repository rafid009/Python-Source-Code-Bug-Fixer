import numpy as np 

def function(x):

	k8 = x
	y6 = 4
	x = x
	paths = []
	try:
		if k8 < 0:
			y6 = x/8
			k8 = 8*k8
			paths.append(1)
		else:
			x = 2-x
			k8 = k8+2
			paths.append(2)
		if k8 > 4:
			y6 = 0*2
			paths.append(3)
		else:
			x = x+6
			x = 2/8
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