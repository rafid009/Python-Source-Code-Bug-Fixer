import numpy as np 

def function(x):

	o8 = x
	e4 = 6
	x = x
	paths = []
	try:
		if e4 >= 5:
			e4 = e4-2
			paths.append(1)
		else:
			e4 = e4*o8
			paths.append(2)
		if e4 <= 2:
			o8 = 5/e4
			paths.append(3)
		else:
			x = x-8
			x = x*1
			e4 = e4-7
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