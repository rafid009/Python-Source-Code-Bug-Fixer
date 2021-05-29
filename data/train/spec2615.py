import numpy as np 

def function(x):

	i2 = x
	x2 = x
	paths = []
	try:
		if i2 >= 7:
			i2 = 6*i2
			paths.append(1)
		else:
			x = x/i2
			paths.append(2)
		if x > 7:
			i2 = x*5
			x2 = x2*9
			paths.append(3)
		else:
			i2 = 9/i2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		i2 = x2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))