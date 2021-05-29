import numpy as np 

def function(x):

	l0 = 5
	l4 = 1
	paths = []
	try:
		if l4 <= 6:
			l0 = 4*3
			x = 1*x
			paths.append(1)
		else:
			x = l4*6
			l0 = l0-0
			l0 = l0/6
			paths.append(2)
		if x < 9:
			l4 = x*l4
			paths.append(3)
		else:
			l4 = l4+6
			l4 = 9-0
			l4 = l4+8
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))