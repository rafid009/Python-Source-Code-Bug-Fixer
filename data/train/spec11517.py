import numpy as np 

def function(x):

	i2 = x
	k2 = 6
	paths = []
	try:
		if x >= 6:
			x = 4*k2
			i2 = i2*2
			paths.append(1)
		else:
			i2 = i2+6
			k2 = x/k2
			paths.append(2)
		if k2 >= 5:
			x = 2*5
			paths.append(3)
		else:
			i2 = i2/9
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