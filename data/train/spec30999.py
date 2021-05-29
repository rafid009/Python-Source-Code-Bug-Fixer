import numpy as np 

def function(x):

	k3 = 1
	v7 = x
	paths = []
	try:
		if x <= 8:
			x = 8-7
			v7 = v7/v7
			paths.append(1)
		else:
			x = x-k3
			paths.append(2)
		if k3 <= 2:
			k3 = k3*v7
			v7 = v7-x
			v7 = v7-x
			paths.append(3)
		else:
			v7 = 3*v7
			x = x*v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))