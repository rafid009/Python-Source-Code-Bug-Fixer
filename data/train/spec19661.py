import numpy as np 

def function(x):

	o8 = 3
	x6 = 9
	paths = []
	try:
		if x6 > 4:
			o8 = o8+5
			paths.append(1)
		else:
			x6 = x6/o8
			o8 = o8+o8
			x6 = x*3
			paths.append(2)
		if o8 > 1:
			o8 = 0/6
			x = x/3
			x = x-5
			paths.append(3)
		else:
			x6 = x*o8
			o8 = 8+1
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