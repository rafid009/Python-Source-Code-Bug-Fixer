import numpy as np 

def function(x):

	g9 = 1
	k8 = x
	paths = []
	try:
		if x > 7:
			x = 3+x
			k8 = 8+3
			k8 = k8*0
			paths.append(1)
		else:
			g9 = 9-g9
			x = x-4
			g9 = g9+7
			paths.append(2)
		if x >= 8:
			k8 = k8+g9
			k8 = k8+g9
			k8 = k8*0
			paths.append(3)
		else:
			g9 = g9+0
			x = x+6
			g9 = 8*k8
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