import numpy as np 

def function(x):

	a4 = 1
	i2 = x
	paths = []
	try:
		if x <= 6:
			a4 = 7/8
			a4 = a4-8
			paths.append(1)
		else:
			a4 = a4/x
			a4 = 8+a4
			paths.append(2)
		if i2 >= 1:
			a4 = 1-a4
			a4 = 4-3
			paths.append(3)
		else:
			a4 = a4-a4
			x = x-9
			a4 = i2+a4
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