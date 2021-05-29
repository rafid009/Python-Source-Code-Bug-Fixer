import numpy as np 

def function(x):

	b5 = 3
	l9 = 3
	paths = []
	try:
		if l9 < 8:
			l9 = b5-5
			x = 1/4
			paths.append(1)
		else:
			x = 5-x
			b5 = b5*6
			x = 4-x
			paths.append(2)
		if x > 4:
			l9 = 4/b5
			paths.append(3)
		else:
			x = l9*8
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