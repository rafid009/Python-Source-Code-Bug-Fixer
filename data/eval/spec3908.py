import numpy as np 

def function(x):

	f0 = x
	w0 = x
	paths = []
	try:
		if f0 <= 6:
			x = 0+x
			f0 = 4*3
			paths.append(1)
		else:
			w0 = w0-7
			paths.append(2)
		if x > 8:
			f0 = f0*f0
			f0 = f0*1
			f0 = x-4
			paths.append(3)
		else:
			w0 = f0/w0
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