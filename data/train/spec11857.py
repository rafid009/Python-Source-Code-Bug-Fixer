import numpy as np 

def function(x):

	l8 = 4
	l4 = x
	x = 8
	paths = []
	try:
		if l8 < 3:
			l8 = l8*2
			l4 = 9*l4
			l8 = x+3
			paths.append(1)
		else:
			x = 5*9
			x = x-l8
			paths.append(2)
		if x <= 3:
			x = l8/1
			paths.append(3)
		else:
			l4 = 9*l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l8 = l4**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))