import numpy as np 

def function(x):

	b4 = 5
	l9 = 2
	paths = []
	try:
		if l9 > 2:
			b4 = b4*l9
			paths.append(1)
		else:
			b4 = 1/x
			l9 = l9-8
			x = x-9
			paths.append(2)
		if l9 <= 1:
			l9 = l9-7
			l9 = 0-l9
			x = b4-x
			paths.append(3)
		else:
			x = l9/l9
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