import numpy as np 

def function(x):

	q7 = x
	k8 = x
	paths = []
	try:
		if x <= 2:
			q7 = q7/3
			q7 = k8-5
			paths.append(1)
		else:
			k8 = x-3
			paths.append(2)
		if k8 >= 6:
			x = 3*7
			paths.append(3)
		else:
			k8 = 7/q7
			x = q7+x
			x = q7-8
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		q7 = k8**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))