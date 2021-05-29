import numpy as np 

def function(x):

	f8 = x
	d1 = x
	paths = []
	try:
		if x > 4:
			x = x+f8
			paths.append(1)
		else:
			x = x+8
			d1 = f8+x
			f8 = f8-4
			paths.append(2)
		if d1 > 1:
			f8 = 8*x
			paths.append(3)
		else:
			x = 9/x
			f8 = 8+f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))