import numpy as np 

def function(x):

	i2 = 1
	v7 = 5
	x = x
	paths = []
	try:
		if x >= 1:
			v7 = x/i2
			i2 = i2/7
			i2 = i2-7
			paths.append(1)
		else:
			x = i2-4
			x = x/8
			paths.append(2)
		if x <= 7:
			v7 = x-v7
			paths.append(3)
		else:
			i2 = i2-6
			x = x+7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		v7 = i2**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))