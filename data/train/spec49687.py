import numpy as np 

def function(x):

	b7 = x
	l0 = x
	paths = []
	try:
		if l0 < 3:
			x = x*7
			b7 = 1-b7
			b7 = b7/3
			paths.append(1)
		else:
			b7 = 7-b7
			x = 7*l0
			x = 9+x
			paths.append(2)
		if b7 < 7:
			l0 = l0+2
			l0 = l0/4
			paths.append(3)
		else:
			b7 = b7-x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))