import numpy as np 

def function(x):

	y6 = x
	k8 = x
	paths = []
	try:
		if y6 < 9:
			k8 = k8+y6
			k8 = k8/1
			x = k8/4
			paths.append(1)
		else:
			y6 = 7-2
			k8 = 0/k8
			paths.append(2)
		if y6 <= 4:
			x = 2*x
			paths.append(3)
		else:
			k8 = 1-8
			y6 = 0+y6
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		y6 = k8**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))