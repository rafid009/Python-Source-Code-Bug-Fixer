import numpy as np 

def function(x):

	k8 = 7
	i9 = x
	x = x
	paths = []
	try:
		if k8 > 1:
			x = 1/x
			paths.append(1)
		else:
			i9 = 6+i9
			k8 = 0-k8
			x = i9*4
			paths.append(2)
		if k8 >= 5:
			x = x+0
			x = k8/6
			x = x-9
			paths.append(3)
		else:
			k8 = x/2
			k8 = 8-x
			i9 = i9+i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))