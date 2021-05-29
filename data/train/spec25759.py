import numpy as np 

def function(x):

	b0 = 2
	f3 = x
	paths = []
	try:
		if b0 >= 8:
			b0 = f3+b0
			paths.append(1)
		else:
			b0 = b0+x
			f3 = f3*f3
			b0 = b0/x
			paths.append(2)
		if b0 <= 9:
			b0 = b0-x
			f3 = f3*b0
			x = x-0
			paths.append(3)
		else:
			x = b0*x
			f3 = b0-f3
			f3 = 8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))