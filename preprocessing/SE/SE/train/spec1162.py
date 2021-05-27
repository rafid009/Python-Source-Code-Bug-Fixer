import numpy as np 

def function(x):

	k8 = 6
	k6 = x
	paths = []
	try:
		if x > 1:
			x = 8-x
			k6 = k6+8
			x = x+2
			paths.append(1)
		else:
			x = 6+x
			k8 = 8-k6
			paths.append(2)
		if k6 >= 4:
			k8 = k8+6
			k6 = k6*k6
			paths.append(3)
		else:
			k8 = k8*9
			k8 = k8+6
			x = 0/8
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))