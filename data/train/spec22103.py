import numpy as np 

def function(x):

	k3 = x
	x2 = 1
	paths = []
	try:
		if x2 < 2:
			k3 = k3*5
			paths.append(1)
		else:
			x = 5/k3
			x2 = x2-7
			paths.append(2)
		if x >= 9:
			x2 = x2/7
			x2 = k3*x
			x = x-0
			paths.append(3)
		else:
			k3 = x+x2
			k3 = k3+0
			x2 = 3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))