import numpy as np 

def function(x):

	j6 = x
	k8 = x
	paths = []
	try:
		if k8 > 5:
			x = 3/j6
			k8 = x/j6
			x = 6*x
			paths.append(1)
		else:
			x = x-6
			x = x-5
			paths.append(2)
		if x > 1:
			j6 = k8+3
			x = x-2
			k8 = k8+k8
			paths.append(3)
		else:
			x = x-2
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