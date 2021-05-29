import numpy as np 

def function(x):

	x4 = 6
	k8 = 8
	x = x
	paths = []
	try:
		if x4 > 8:
			x4 = 9*6
			paths.append(1)
		else:
			x4 = x4-4
			x4 = 5*x4
			paths.append(2)
		if x4 <= 9:
			x4 = x4-2
			x4 = k8*0
			k8 = 5-k8
			paths.append(3)
		else:
			k8 = 7*k8
			x = x+7
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