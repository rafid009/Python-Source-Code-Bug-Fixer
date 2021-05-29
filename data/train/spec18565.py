import numpy as np 

def function(x):

	k3 = 5
	l4 = 3
	paths = []
	try:
		if x < 1:
			x = x+l4
			paths.append(1)
		else:
			x = x/2
			l4 = 5-l4
			x = k3-7
			paths.append(2)
		if l4 >= 6:
			l4 = k3*x
			k3 = 0*9
			paths.append(3)
		else:
			x = x+7
			k3 = k3/k3
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