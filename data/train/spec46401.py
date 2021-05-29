import numpy as np 

def function(x):

	f8 = 7
	y0 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = 7/x
			f8 = f8-5
			paths.append(1)
		else:
			f8 = f8+5
			f8 = f8/f8
			paths.append(2)
		if f8 >= 0:
			y0 = x+4
			paths.append(3)
		else:
			x = x+9
			f8 = 1-f8
			f8 = 5/f8
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