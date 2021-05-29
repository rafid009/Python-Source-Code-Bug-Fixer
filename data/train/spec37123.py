import numpy as np 

def function(x):

	k3 = x
	x9 = 3
	paths = []
	try:
		if x9 <= 5:
			k3 = k3*5
			x9 = x9/k3
			paths.append(1)
		else:
			x = 3*x
			x9 = x9+k3
			paths.append(2)
		if k3 >= 6:
			x = k3+6
			paths.append(3)
		else:
			x9 = 1-x9
			k3 = 8-k3
			k3 = 8+8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		k3 = x9**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))