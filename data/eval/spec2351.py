import numpy as np 

def function(x):

	j1 = x
	k0 = 5
	paths = []
	try:
		if j1 >= 4:
			k0 = j1-9
			j1 = 1-x
			k0 = k0/8
			paths.append(1)
		else:
			k0 = k0-1
			k0 = x+k0
			j1 = j1-k0
			paths.append(2)
		if k0 > 1:
			j1 = 5/j1
			x = x/k0
			j1 = j1/j1
			paths.append(3)
		else:
			k0 = 5/j1
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))