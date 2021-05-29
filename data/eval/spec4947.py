import numpy as np 

def function(x):

	k8 = x
	r6 = 3
	paths = []
	try:
		if r6 > 2:
			r6 = r6*r6
			k8 = r6/9
			paths.append(1)
		else:
			k8 = 7/9
			k8 = 9+r6
			r6 = r6-1
			paths.append(2)
		if x > 0:
			k8 = k8-0
			paths.append(3)
		else:
			k8 = k8-8
			x = x+k8
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