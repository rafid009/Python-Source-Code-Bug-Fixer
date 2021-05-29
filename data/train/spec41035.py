import numpy as np 

def function(x):

	k3 = 8
	n4 = 2
	paths = []
	try:
		if n4 >= 2:
			n4 = n4+4
			x = x/4
			paths.append(1)
		else:
			x = k3/x
			x = x/2
			paths.append(2)
		if n4 >= 5:
			n4 = 1-n4
			n4 = 8/n4
			k3 = 6/k3
			paths.append(3)
		else:
			n4 = n4*3
			x = 4*7
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		k3 = n4**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))