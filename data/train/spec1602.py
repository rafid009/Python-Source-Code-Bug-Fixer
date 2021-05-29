import numpy as np 

def function(x):

	b1 = x
	l4 = 0
	paths = []
	try:
		if b1 < 3:
			x = l4*7
			x = l4/2
			b1 = x+4
			paths.append(1)
		else:
			b1 = b1-9
			paths.append(2)
		if b1 <= 3:
			l4 = l4+9
			paths.append(3)
		else:
			l4 = l4+l4
			x = l4*x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		l4 = b1**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))