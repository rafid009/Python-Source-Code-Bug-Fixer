import numpy as np 

def function(x):

	n8 = x
	k8 = 9
	paths = []
	try:
		if x <= 0:
			k8 = 4-k8
			paths.append(1)
		else:
			n8 = n8*1
			k8 = k8/9
			x = k8/n8
			paths.append(2)
		if x < 2:
			x = 9*3
			paths.append(3)
		else:
			n8 = 9*4
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		k8 = n8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))