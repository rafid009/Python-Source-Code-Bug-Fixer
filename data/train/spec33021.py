import numpy as np 

def function(x):

	l8 = 4
	b7 = x
	paths = []
	try:
		if b7 < 9:
			l8 = l8/8
			x = b7-7
			x = 5+1
			paths.append(1)
		else:
			x = 7+0
			l8 = 2+3
			l8 = 2+5
			paths.append(2)
		if x < 7:
			x = x/b7
			paths.append(3)
		else:
			b7 = b7-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))