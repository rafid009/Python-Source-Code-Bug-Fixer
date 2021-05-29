import numpy as np 

def function(x):

	b0 = x
	l6 = 2
	paths = []
	try:
		if x < 3:
			b0 = b0*7
			paths.append(1)
		else:
			b0 = 9/x
			b0 = b0-b0
			x = x+b0
			paths.append(2)
		if x > 0:
			x = 1+x
			b0 = 0-b0
			b0 = 1+l6
			paths.append(3)
		else:
			b0 = 1+b0
			l6 = 8*l6
			x = 5/9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))