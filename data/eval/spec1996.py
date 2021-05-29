import numpy as np 

def function(x):

	o8 = x
	i2 = 7
	paths = []
	try:
		if i2 > 2:
			o8 = 3-o8
			o8 = o8*7
			i2 = 1*x
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if o8 < 5:
			i2 = i2-3
			paths.append(3)
		else:
			o8 = 3*o8
			x = o8-x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		o8 = i2**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))