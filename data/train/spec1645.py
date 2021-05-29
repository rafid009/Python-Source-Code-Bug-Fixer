import numpy as np 

def function(x):

	f4 = 0
	b1 = 8
	paths = []
	try:
		if b1 <= 1:
			b1 = x*f4
			paths.append(1)
		else:
			f4 = b1-7
			paths.append(2)
		if f4 < 8:
			b1 = x+6
			b1 = b1+2
			x = 9-x
			paths.append(3)
		else:
			b1 = b1-3
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