import numpy as np 

def function(x):

	f4 = x
	x3 = 3
	paths = []
	try:
		if x >= 6:
			x = x-9
			f4 = f4-5
			paths.append(1)
		else:
			x3 = 7/x3
			paths.append(2)
		if x < 1:
			x = x-9
			x3 = 2-x3
			f4 = f4/2
			paths.append(3)
		else:
			f4 = x-f4
			f4 = x/6
			f4 = f4*x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		f4 = x3**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))