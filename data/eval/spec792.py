import numpy as np 

def function(x):

	l9 = 6
	f5 = 5
	paths = []
	try:
		if f5 >= 1:
			l9 = l9+6
			l9 = 4+l9
			paths.append(1)
		else:
			x = 0*x
			f5 = x-f5
			f5 = 5/f5
			paths.append(2)
		if f5 >= 3:
			f5 = x+6
			f5 = 2*f5
			paths.append(3)
		else:
			x = l9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))