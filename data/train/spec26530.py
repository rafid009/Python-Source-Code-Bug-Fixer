import numpy as np 

def function(x):

	f0 = x
	l1 = 5
	paths = []
	try:
		if l1 < 0:
			x = 0-x
			f0 = f0-6
			x = 3/x
			paths.append(1)
		else:
			x = 6+x
			x = x/l1
			paths.append(2)
		if f0 < 8:
			x = 6*x
			f0 = 0/f0
			f0 = 4+f0
			paths.append(3)
		else:
			x = 1+4
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