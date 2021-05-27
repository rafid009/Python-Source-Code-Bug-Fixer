import numpy as np 

def function(x):

	l6 = x
	b2 = 2
	paths = []
	try:
		if l6 <= 0:
			x = 7*x
			b2 = 1+b2
			l6 = 2+b2
			paths.append(1)
		else:
			x = 0-b2
			l6 = l6-9
			paths.append(2)
		if l6 < 0:
			b2 = b2/8
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))