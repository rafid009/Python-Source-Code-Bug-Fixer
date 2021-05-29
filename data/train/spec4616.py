import numpy as np 

def function(x):

	k3 = 7
	t6 = 1
	paths = []
	try:
		if x > 3:
			k3 = t6/k3
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x > 9:
			k3 = k3*k3
			k3 = k3/2
			x = 2-x
			paths.append(3)
		else:
			k3 = 1+k3
			k3 = 7*t6
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