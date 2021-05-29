import numpy as np 

def function(x):

	b0 = 8
	i2 = x
	paths = []
	try:
		if b0 > 5:
			x = x-9
			i2 = i2-4
			paths.append(1)
		else:
			b0 = 3-b0
			paths.append(2)
		if i2 > 4:
			b0 = b0-8
			paths.append(3)
		else:
			b0 = b0/3
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))