import numpy as np 

def function(x):

	i9 = x
	k0 = 8
	paths = []
	try:
		if i9 <= 4:
			k0 = k0+x
			x = x-i9
			paths.append(1)
		else:
			x = i9/x
			x = 2-x
			k0 = k0-k0
			paths.append(2)
		if k0 < 5:
			x = 2+5
			paths.append(3)
		else:
			k0 = k0/k0
			i9 = 5*7
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