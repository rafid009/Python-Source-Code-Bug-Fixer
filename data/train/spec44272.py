import numpy as np 

def function(x):

	l6 = x
	b8 = 1
	paths = []
	try:
		if l6 >= 1:
			l6 = x-7
			paths.append(1)
		else:
			l6 = l6-x
			x = l6-2
			paths.append(2)
		if x > 0:
			x = x*b8
			l6 = 4-l6
			b8 = b8-l6
			paths.append(3)
		else:
			x = 7*b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))