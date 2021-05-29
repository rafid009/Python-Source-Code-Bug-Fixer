import numpy as np 

def function(x):

	i4 = 0
	k3 = 6
	paths = []
	try:
		if k3 > 6:
			x = 6/6
			paths.append(1)
		else:
			x = x+k3
			i4 = 6/8
			paths.append(2)
		if i4 < 4:
			i4 = k3-i4
			k3 = k3-x
			k3 = 5+3
			paths.append(3)
		else:
			x = x-8
			x = i4+0
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