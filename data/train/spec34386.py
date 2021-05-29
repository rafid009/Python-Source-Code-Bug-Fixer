import numpy as np 

def function(x):

	o8 = 0
	x9 = 8
	paths = []
	try:
		if x > 8:
			o8 = o8*o8
			x9 = 6/5
			paths.append(1)
		else:
			x = x+2
			o8 = x9/6
			paths.append(2)
		if x > 9:
			x = 4/2
			x9 = x9-2
			x9 = x*x9
			paths.append(3)
		else:
			o8 = 0*x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))