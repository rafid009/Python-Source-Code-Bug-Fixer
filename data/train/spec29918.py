import numpy as np 

def function(x):

	l4 = 1
	b0 = 4
	paths = []
	try:
		if x > 3:
			b0 = x*b0
			paths.append(1)
		else:
			l4 = 7+l4
			x = 2-x
			paths.append(2)
		if b0 <= 2:
			x = x/x
			paths.append(3)
		else:
			b0 = 3-b0
			x = 9-x
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