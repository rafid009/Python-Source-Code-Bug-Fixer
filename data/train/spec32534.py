import numpy as np 

def function(x):

	b0 = x
	f1 = x
	paths = []
	try:
		if b0 > 1:
			x = 2*x
			f1 = f1-b0
			paths.append(1)
		else:
			x = x+x
			b0 = b0*1
			paths.append(2)
		if b0 < 8:
			f1 = f1-x
			b0 = 0+b0
			paths.append(3)
		else:
			x = x+2
			f1 = b0-8
			b0 = f1-f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))