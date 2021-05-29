import numpy as np 

def function(x):

	u4 = x
	k8 = 8
	paths = []
	try:
		if x >= 0:
			k8 = u4*u4
			k8 = 4-k8
			x = 5+u4
			paths.append(1)
		else:
			k8 = 7-k8
			paths.append(2)
		if k8 > 0:
			x = 5*1
			u4 = k8+9
			paths.append(3)
		else:
			x = x+3
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