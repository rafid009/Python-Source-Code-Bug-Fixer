import numpy as np 

def function(x):

	g7 = x
	k8 = x
	paths = []
	try:
		if k8 > 9:
			x = x-3
			paths.append(1)
		else:
			g7 = g7+g7
			x = x/4
			paths.append(2)
		if x <= 5:
			k8 = k8-g7
			g7 = 5-x
			paths.append(3)
		else:
			k8 = k8+4
			g7 = g7*3
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