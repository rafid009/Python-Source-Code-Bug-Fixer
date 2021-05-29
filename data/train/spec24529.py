import numpy as np 

def function(x):

	e2 = x
	o8 = 5
	paths = []
	try:
		if o8 <= 7:
			e2 = e2*1
			o8 = 0-o8
			e2 = e2*e2
			paths.append(1)
		else:
			e2 = 1/e2
			paths.append(2)
		if o8 < 7:
			o8 = o8*o8
			o8 = 7*o8
			paths.append(3)
		else:
			e2 = x/6
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