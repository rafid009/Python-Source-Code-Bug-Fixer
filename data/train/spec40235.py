import numpy as np 

def function(x):

	k8 = x
	q9 = x
	paths = []
	try:
		if x >= 9:
			k8 = x*6
			x = 3-q9
			x = 3/3
			paths.append(1)
		else:
			x = x*q9
			k8 = 6+k8
			x = 6+9
			paths.append(2)
		if q9 >= 4:
			k8 = k8-3
			q9 = 2-x
			x = 1*q9
			paths.append(3)
		else:
			k8 = k8*4
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))