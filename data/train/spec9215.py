import numpy as np 

def function(x):

	l8 = 3
	k0 = x
	paths = []
	try:
		if x > 0:
			l8 = l8-x
			paths.append(1)
		else:
			k0 = x*1
			k0 = k0+2
			x = 7+x
			paths.append(2)
		if l8 > 3:
			l8 = l8-8
			paths.append(3)
		else:
			x = x-5
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))