import numpy as np 

def function(x):

	z9 = x
	i2 = 2
	paths = []
	try:
		if x >= 3:
			x = x-4
			i2 = x/i2
			i2 = i2-1
			paths.append(1)
		else:
			i2 = i2-x
			paths.append(2)
		if z9 >= 1:
			i2 = 6/3
			paths.append(3)
		else:
			i2 = z9-6
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))