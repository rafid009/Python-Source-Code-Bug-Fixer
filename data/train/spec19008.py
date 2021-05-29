import numpy as np 

def function(x):

	k8 = x
	o3 = x
	paths = []
	try:
		if k8 < 1:
			k8 = k8+o3
			o3 = 0/6
			o3 = x-4
			paths.append(1)
		else:
			k8 = o3*1
			k8 = o3-6
			paths.append(2)
		if o3 >= 2:
			k8 = x*7
			x = x*2
			paths.append(3)
		else:
			x = 2+x
			k8 = k8-o3
			k8 = k8-x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))