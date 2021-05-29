import numpy as np 

def function(x):

	a4 = x
	k3 = 8
	paths = []
	try:
		if a4 >= 6:
			k3 = k3/k3
			paths.append(1)
		else:
			k3 = 1/8
			paths.append(2)
		if x <= 8:
			k3 = k3+x
			paths.append(3)
		else:
			a4 = a4-5
			x = 3/x
			a4 = 7/8
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		a4 = k3**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))