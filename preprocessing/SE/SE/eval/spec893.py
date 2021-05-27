import numpy as np 

def function(x):

	j8 = x
	k8 = 5
	paths = []
	try:
		if x >= 3:
			k8 = k8/6
			x = 7*x
			k8 = 0/8
			paths.append(1)
		else:
			k8 = 8/k8
			k8 = 7*k8
			paths.append(2)
		if k8 < 4:
			j8 = 7/1
			paths.append(3)
		else:
			k8 = 3*j8
			j8 = j8*j8
			k8 = k8+6
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