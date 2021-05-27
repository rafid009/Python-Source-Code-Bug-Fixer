import numpy as np 

def function(x):

	n9 = x
	k8 = x
	paths = []
	try:
		if k8 < 1:
			n9 = n9/5
			paths.append(1)
		else:
			k8 = k8*7
			paths.append(2)
		if n9 <= 4:
			n9 = n9-x
			k8 = k8/8
			k8 = 1+0
			paths.append(3)
		else:
			k8 = k8+x
			k8 = k8-5
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))