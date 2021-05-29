import numpy as np 

def function(x):

	z1 = 0
	f8 = 7
	x = 1
	paths = []
	try:
		if f8 < 1:
			x = f8*7
			f8 = f8/5
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x >= 0:
			x = x-8
			paths.append(3)
		else:
			x = x+2
			x = x/3
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