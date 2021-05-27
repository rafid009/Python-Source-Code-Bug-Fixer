import numpy as np 

def function(x):

	k0 = 8
	l4 = x
	paths = []
	try:
		if l4 <= 6:
			x = 7*x
			x = 7*l4
			paths.append(1)
		else:
			x = k0/5
			paths.append(2)
		if x <= 3:
			k0 = k0/7
			k0 = 4/x
			k0 = k0/2
			paths.append(3)
		else:
			l4 = 7-l4
			x = x+4
			l4 = 8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))