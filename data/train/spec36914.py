import numpy as np 

def function(x):

	k8 = 0
	y7 = 2
	paths = []
	try:
		if x > 3:
			y7 = x/1
			paths.append(1)
		else:
			k8 = y7+x
			paths.append(2)
		if y7 > 0:
			x = 0+7
			k8 = 2*k8
			y7 = 4*x
			paths.append(3)
		else:
			y7 = y7*6
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