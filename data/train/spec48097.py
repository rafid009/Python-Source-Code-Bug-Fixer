import numpy as np 

def function(x):

	b0 = 8
	l5 = x
	paths = []
	try:
		if b0 < 2:
			l5 = l5-2
			l5 = l5-0
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if l5 > 3:
			x = x-6
			l5 = l5*3
			paths.append(3)
		else:
			b0 = b0/l5
			x = b0-3
			b0 = b0-2
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