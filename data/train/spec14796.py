import numpy as np 

def function(x):

	b9 = 0
	i2 = x
	paths = []
	try:
		if b9 > 5:
			b9 = i2/b9
			paths.append(1)
		else:
			i2 = i2*6
			i2 = 1-i2
			b9 = 9/3
			paths.append(2)
		if b9 >= 7:
			b9 = b9-b9
			x = x-i2
			paths.append(3)
		else:
			i2 = 4*b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))