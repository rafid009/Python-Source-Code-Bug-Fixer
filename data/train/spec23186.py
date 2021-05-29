import numpy as np 

def function(x):

	i2 = 6
	x6 = 6
	paths = []
	try:
		if x <= 2:
			i2 = i2+0
			x = 6*7
			paths.append(1)
		else:
			x6 = x6-x
			i2 = i2+x6
			paths.append(2)
		if x <= 1:
			x = 1-9
			x = x+5
			paths.append(3)
		else:
			x = x-7
			x6 = x6-7
			i2 = i2-3
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))