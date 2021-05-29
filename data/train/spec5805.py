import numpy as np 

def function(x):

	f2 = x
	o8 = 0
	paths = []
	try:
		if o8 >= 0:
			o8 = o8*8
			paths.append(1)
		else:
			o8 = o8*o8
			paths.append(2)
		if x >= 1:
			f2 = x+f2
			paths.append(3)
		else:
			o8 = o8+f2
			o8 = o8-o8
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