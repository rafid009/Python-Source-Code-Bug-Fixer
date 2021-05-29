import numpy as np 

def function(x):

	k8 = x
	q3 = x
	x = 6
	paths = []
	try:
		if x <= 6:
			x = 7+q3
			q3 = q3+6
			k8 = k8*8
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if k8 > 9:
			x = 6*q3
			q3 = q3/6
			k8 = k8*k8
			paths.append(3)
		else:
			q3 = k8*0
			k8 = 7-k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))