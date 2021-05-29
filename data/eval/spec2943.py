import numpy as np 

def function(x):

	i2 = x
	k0 = 7
	paths = []
	try:
		if i2 >= 3:
			x = x*9
			k0 = k0/1
			paths.append(1)
		else:
			i2 = 2*i2
			paths.append(2)
		if i2 < 8:
			k0 = 9-k0
			x = 7/i2
			paths.append(3)
		else:
			i2 = i2+1
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