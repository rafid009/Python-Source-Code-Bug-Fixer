import numpy as np 

def function(x):

	k8 = 7
	v5 = x
	paths = []
	try:
		if x > 7:
			x = k8/x
			k8 = k8*k8
			paths.append(1)
		else:
			v5 = x-v5
			v5 = 9-v5
			v5 = v5+x
			paths.append(2)
		if k8 >= 1:
			x = 6-1
			x = 3/x
			k8 = 7*k8
			paths.append(3)
		else:
			k8 = v5-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		k8 = v5**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))