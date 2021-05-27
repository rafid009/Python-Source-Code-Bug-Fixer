import numpy as np 

def function(x):

	b4 = 9
	k3 = 3
	paths = []
	try:
		if b4 < 0:
			x = 5/x
			x = 9-8
			paths.append(1)
		else:
			b4 = x/b4
			k3 = b4-x
			paths.append(2)
		if b4 >= 9:
			x = 3-b4
			paths.append(3)
		else:
			x = x-0
			k3 = k3-2
			b4 = x*b4
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