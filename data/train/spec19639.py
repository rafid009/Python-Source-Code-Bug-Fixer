import numpy as np 

def function(x):

	b2 = x
	l6 = x
	paths = []
	try:
		if l6 < 0:
			l6 = l6+6
			b2 = 9*b2
			paths.append(1)
		else:
			l6 = l6+5
			paths.append(2)
		if b2 < 6:
			x = x-1
			b2 = b2*3
			paths.append(3)
		else:
			b2 = b2*9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))