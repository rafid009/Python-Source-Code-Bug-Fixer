import numpy as np 

def function(x):

	q9 = 0
	k8 = 2
	paths = []
	try:
		if q9 >= 2:
			x = 2*x
			paths.append(1)
		else:
			k8 = 5+k8
			paths.append(2)
		if q9 < 2:
			q9 = 3-k8
			q9 = q9-9
			paths.append(3)
		else:
			x = 7+8
			q9 = 9-x
			k8 = 6-q9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		k8 = q9**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))