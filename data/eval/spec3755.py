import numpy as np 

def function(x):

	d0 = 5
	f6 = x
	paths = []
	try:
		if d0 >= 4:
			f6 = 2*f6
			x = x-7
			paths.append(1)
		else:
			f6 = x*f6
			paths.append(2)
		if x > 6:
			f6 = 8/f6
			f6 = 5*f6
			paths.append(3)
		else:
			x = x*d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))