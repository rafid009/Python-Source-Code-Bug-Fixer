import numpy as np 

def function(x):

	u1 = 7
	k8 = 0
	paths = []
	try:
		if u1 >= 5:
			k8 = 6+k8
			k8 = k8/u1
			paths.append(1)
		else:
			k8 = x*3
			k8 = k8-9
			x = 9/x
			paths.append(2)
		if u1 <= 3:
			x = x*x
			paths.append(3)
		else:
			k8 = k8-6
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