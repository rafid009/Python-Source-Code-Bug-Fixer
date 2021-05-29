import numpy as np 

def function(x):

	i9 = 5
	k3 = 5
	x = x
	paths = []
	try:
		if k3 > 2:
			i9 = k3*i9
			k3 = k3/i9
			k3 = x-k3
			paths.append(1)
		else:
			i9 = k3+4
			i9 = x-5
			paths.append(2)
		if i9 <= 0:
			i9 = k3/i9
			i9 = i9*k3
			paths.append(3)
		else:
			x = 9-k3
			x = i9-x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		i9 = k3**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))