import numpy as np 

def function(x):

	k8 = x
	u4 = 9
	paths = []
	try:
		if x >= 9:
			x = x-0
			k8 = u4+k8
			paths.append(1)
		else:
			k8 = k8/9
			paths.append(2)
		if k8 >= 8:
			u4 = 2-3
			x = 0*k8
			paths.append(3)
		else:
			k8 = x*3
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		u4 = k8**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))