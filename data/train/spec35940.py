import numpy as np 

def function(x):

	l4 = 4
	k0 = 6
	paths = []
	try:
		if x > 3:
			l4 = 8/l4
			k0 = k0*x
			paths.append(1)
		else:
			x = 1+x
			l4 = l4*k0
			x = x/5
			paths.append(2)
		if x < 8:
			x = x-9
			x = x/k0
			paths.append(3)
		else:
			x = x/7
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