import numpy as np 

def function(x):

	f6 = x
	o8 = 7
	paths = []
	try:
		if x < 3:
			f6 = 6/f6
			paths.append(1)
		else:
			o8 = 8-o8
			paths.append(2)
		if o8 < 4:
			x = f6+x
			paths.append(3)
		else:
			f6 = 7*f6
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