import numpy as np 

def function(x):

	j1 = x
	k8 = 0
	paths = []
	try:
		if x <= 4:
			x = x/9
			paths.append(1)
		else:
			k8 = 4-j1
			k8 = 2/3
			paths.append(2)
		if x < 9:
			k8 = 8-9
			paths.append(3)
		else:
			x = j1-2
			k8 = 5-k8
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