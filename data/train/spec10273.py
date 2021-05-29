import numpy as np 

def function(x):

	y5 = 6
	k8 = x
	paths = []
	try:
		if x > 4:
			k8 = k8/y5
			paths.append(1)
		else:
			y5 = y5/k8
			y5 = y5/8
			paths.append(2)
		if y5 <= 1:
			y5 = x-7
			y5 = 0-3
			paths.append(3)
		else:
			x = 5-x
			k8 = 0*k8
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))