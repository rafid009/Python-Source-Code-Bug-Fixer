import numpy as np 

def function(x):

	o8 = 4
	i2 = 7
	paths = []
	try:
		if x >= 9:
			o8 = o8*4
			x = x/o8
			paths.append(1)
		else:
			o8 = o8*1
			paths.append(2)
		if i2 > 9:
			x = i2+x
			paths.append(3)
		else:
			i2 = 7+8
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