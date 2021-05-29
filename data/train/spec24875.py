import numpy as np 

def function(x):

	x0 = 7
	k3 = x
	paths = []
	try:
		if x0 >= 3:
			x = 9+3
			x = 1/x
			paths.append(1)
		else:
			k3 = k3-5
			x = x/8
			x = x+1
			paths.append(2)
		if k3 >= 9:
			k3 = k3*3
			x = 3-1
			paths.append(3)
		else:
			k3 = x+k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x0 = k3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))