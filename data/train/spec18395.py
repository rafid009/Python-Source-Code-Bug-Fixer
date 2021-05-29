import numpy as np 

def function(x):

	y3 = 4
	k8 = 8
	paths = []
	try:
		if x >= 9:
			x = x-x
			y3 = 0-y3
			y3 = y3+1
			paths.append(1)
		else:
			x = 6+4
			y3 = 7-k8
			y3 = 9/7
			paths.append(2)
		if x >= 9:
			y3 = 7/y3
			x = 3-6
			paths.append(3)
		else:
			y3 = y3/y3
			x = 4+y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))