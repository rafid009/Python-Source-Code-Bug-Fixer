import numpy as np 

def function(x):

	j9 = 4
	k8 = x
	paths = []
	try:
		if x >= 2:
			x = k8/5
			x = 3*x
			paths.append(1)
		else:
			k8 = k8*7
			j9 = j9*2
			paths.append(2)
		if x < 1:
			j9 = k8/x
			k8 = 0/3
			x = 6/x
			paths.append(3)
		else:
			x = 3*1
			k8 = 2+k8
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