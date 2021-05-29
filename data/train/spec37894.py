import numpy as np 

def function(x):

	f0 = 8
	o7 = x
	paths = []
	try:
		if f0 <= 7:
			o7 = o7/o7
			o7 = 3*o7
			paths.append(1)
		else:
			o7 = o7/9
			x = x-6
			paths.append(2)
		if x >= 0:
			x = x+o7
			f0 = f0-9
			paths.append(3)
		else:
			f0 = f0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))