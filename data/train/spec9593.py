import numpy as np 

def function(x):

	x4 = x
	k9 = x
	paths = []
	try:
		if x4 >= 8:
			x4 = x4/k9
			x = 4*x
			x4 = k9-k9
			paths.append(1)
		else:
			x4 = x/2
			paths.append(2)
		if x > 0:
			k9 = k9-2
			paths.append(3)
		else:
			x = 4*x
			x4 = x4*6
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))