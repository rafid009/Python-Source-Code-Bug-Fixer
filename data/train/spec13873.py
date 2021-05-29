import numpy as np 

def function(x):

	q8 = x
	f4 = 2
	paths = []
	try:
		if f4 > 7:
			f4 = f4-6
			q8 = q8-f4
			paths.append(1)
		else:
			x = f4/q8
			f4 = f4-9
			paths.append(2)
		if x > 4:
			q8 = q8*f4
			x = x-x
			paths.append(3)
		else:
			x = 1/x
			q8 = 0-q8
			f4 = 1*q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))