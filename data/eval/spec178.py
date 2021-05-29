import numpy as np 

def function(x):

	k8 = x
	y4 = x
	paths = []
	try:
		if x < 9:
			x = 0-x
			y4 = y4+6
			paths.append(1)
		else:
			x = x-3
			y4 = 5/y4
			paths.append(2)
		if k8 < 4:
			x = y4-x
			paths.append(3)
		else:
			y4 = y4+2
			y4 = 0-6
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))