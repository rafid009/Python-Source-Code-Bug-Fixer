import numpy as np 

def function(x):

	f0 = 0
	l9 = x
	paths = []
	try:
		if x < 7:
			f0 = f0+8
			x = x-l9
			x = x-x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if l9 < 1:
			f0 = f0+l9
			paths.append(3)
		else:
			l9 = l9-f0
			l9 = l9*l9
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