import numpy as np 

def function(x):

	k1 = x
	k8 = 6
	paths = []
	try:
		if x < 7:
			k8 = k8/k1
			k8 = 9+x
			x = 1/9
			paths.append(1)
		else:
			x = 0*x
			x = 4/7
			x = 4-8
			paths.append(2)
		if x > 7:
			k8 = x*k8
			k1 = 8-5
			paths.append(3)
		else:
			k1 = k1-8
			k1 = 8+6
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k1 = k8**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))