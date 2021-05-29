import numpy as np 

def function(x):

	o8 = x
	p6 = x
	paths = []
	try:
		if x <= 2:
			o8 = 5*o8
			p6 = p6*8
			x = o8*3
			paths.append(1)
		else:
			o8 = o8-9
			paths.append(2)
		if x <= 8:
			x = o8-0
			paths.append(3)
		else:
			x = x*x
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