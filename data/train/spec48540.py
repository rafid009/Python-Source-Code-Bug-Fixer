import numpy as np 

def function(x):

	b4 = x
	l9 = 9
	x = x
	paths = []
	try:
		if x < 7:
			x = 1-9
			l9 = l9-x
			l9 = 0-l9
			paths.append(1)
		else:
			l9 = l9-1
			l9 = l9*4
			l9 = 0+3
			paths.append(2)
		if x > 7:
			l9 = b4-9
			l9 = 6*l9
			paths.append(3)
		else:
			l9 = 8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))