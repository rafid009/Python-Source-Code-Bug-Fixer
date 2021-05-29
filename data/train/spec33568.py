import numpy as np 

def function(x):

	k3 = 5
	i1 = 6
	paths = []
	try:
		if x < 0:
			i1 = i1-k3
			paths.append(1)
		else:
			i1 = x+i1
			i1 = 4*9
			paths.append(2)
		if x <= 7:
			k3 = 9-5
			paths.append(3)
		else:
			i1 = i1+6
			k3 = k3+8
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