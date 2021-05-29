import numpy as np 

def function(x):

	k8 = x
	q8 = 3
	paths = []
	try:
		if k8 > 0:
			k8 = 0+k8
			x = k8+x
			k8 = 5-k8
			paths.append(1)
		else:
			k8 = k8-2
			q8 = x*q8
			k8 = k8-5
			paths.append(2)
		if q8 <= 3:
			x = x+q8
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		q8 = k8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))