import numpy as np 

def function(x):

	k8 = x
	i8 = x
	paths = []
	try:
		if i8 > 4:
			k8 = k8/k8
			k8 = 3+x
			k8 = x/k8
			paths.append(1)
		else:
			k8 = k8+4
			paths.append(2)
		if k8 > 9:
			x = 8-1
			i8 = k8+5
			k8 = 8-5
			paths.append(3)
		else:
			i8 = i8-i8
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