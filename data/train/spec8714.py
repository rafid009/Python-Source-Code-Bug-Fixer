import numpy as np 

def function(x):

	k8 = 3
	i6 = x
	paths = []
	try:
		if i6 >= 7:
			i6 = 6/i6
			i6 = x-4
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if k8 <= 8:
			k8 = k8-i6
			x = x-x
			paths.append(3)
		else:
			x = x*k8
			i6 = 4*i6
			k8 = k8*k8
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))