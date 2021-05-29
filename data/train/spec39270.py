import numpy as np 

def function(x):

	k3 = 1
	i4 = 4
	paths = []
	try:
		if k3 > 8:
			k3 = k3-4
			paths.append(1)
		else:
			k3 = k3-x
			i4 = 5*9
			x = i4+6
			paths.append(2)
		if k3 >= 8:
			i4 = i4-3
			i4 = 3/i4
			paths.append(3)
		else:
			i4 = 6*2
			x = 6+k3
			x = i4*k3
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