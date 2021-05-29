import numpy as np 

def function(x):

	i4 = 4
	k8 = x
	paths = []
	try:
		if k8 > 5:
			k8 = k8*x
			i4 = i4*3
			k8 = 3-k8
			paths.append(1)
		else:
			k8 = 6-k8
			paths.append(2)
		if i4 <= 1:
			x = i4*i4
			x = i4*5
			paths.append(3)
		else:
			i4 = 1/x
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