import numpy as np 

def function(x):

	n6 = 2
	i2 = x
	paths = []
	try:
		if x <= 6:
			n6 = i2/x
			paths.append(1)
		else:
			n6 = n6-7
			n6 = n6*n6
			paths.append(2)
		if x < 6:
			i2 = 5-i2
			x = n6-x
			i2 = i2/8
			paths.append(3)
		else:
			n6 = n6*n6
			i2 = i2-2
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