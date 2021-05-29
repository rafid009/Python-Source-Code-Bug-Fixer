import numpy as np 

def function(x):

	g3 = x
	k8 = 9
	paths = []
	try:
		if k8 >= 3:
			g3 = g3/9
			paths.append(1)
		else:
			k8 = x/k8
			paths.append(2)
		if x <= 7:
			k8 = k8/3
			x = x/5
			paths.append(3)
		else:
			k8 = k8+5
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