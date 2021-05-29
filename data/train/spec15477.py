import numpy as np 

def function(x):

	f6 = 7
	r9 = x
	paths = []
	try:
		if r9 >= 4:
			r9 = 1*8
			paths.append(1)
		else:
			f6 = x-3
			x = 4+5
			x = x/3
			paths.append(2)
		if r9 >= 3:
			r9 = r9+4
			f6 = f6/6
			x = f6-9
			paths.append(3)
		else:
			x = x-8
			f6 = f6/6
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