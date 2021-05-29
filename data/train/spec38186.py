import numpy as np 

def function(x):

	k6 = x
	k8 = 3
	x = x
	paths = []
	try:
		if k8 > 6:
			k8 = 7+k8
			paths.append(1)
		else:
			k8 = k8-4
			paths.append(2)
		if k6 < 0:
			x = k8-x
			k8 = k8-k8
			x = 4*9
			paths.append(3)
		else:
			x = x*0
			k8 = k8+x
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